#!/usr/bin/env python3


import socket
import tkinter as tk


def client_program():
    # Client socket
    host = "localhost"
    port = 12345
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))

    # Input de cliente
    username = input("\n[+] Introduce tu usuario: ")
    # Envia cliente a server
    client_socket.sendall(username.encode())

    window = tk.Tk()
    window.title("Chat")

    window.mainloop()


if __name__ == "__main__":
    client_program()
