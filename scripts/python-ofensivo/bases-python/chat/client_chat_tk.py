#!/usr/bin/env python3

import socket
import threading
import tkinter as tk
from tkinter.scrolledtext import ScrolledText


def send_message(event, client_socket, username, text_widget, entry_widget):
    print(f"\n[+] Se ha presionado la tecla enter")
    message = entry_widget.get()
    print(f"\n[+] El usuario {username}, ha escrito: {message}")
    client_socket.sendall(f"{username} > {message}".encode())
    entry_widget.delete(0, tk.END)
    text_widget.configure(state="normal")
    text_widget.insert(tk.END, f"{username} > {message}\n")
    text_widget.configure(state="disable")


def receive_message(client_socket, text_widget):
    while True:
        try:
            message = client_socket.recv(1024).decode()

            if not message:
                break
            text_widget.configure(state="normal")
            text_widget.insert(tk.END, message)
            text_widget.configure(state="disable")
        except:
            print("error: ")
            break


def client_program():
    host = "localhost"
    port = 12345

    client_socket = socket.socket(socket.AF_INET, socket.SOL_SOCKET)
    client_socket.connect((host, port))

    username = input("Introduce tu nombre de usuario: ")
    client_socket.sendall(username.encode())

    window = tk.Tk()
    window.geometry("1000x1000")
    window.title("Chat")
    # NOTE: State disable desabilita la escritura
    text_widget = ScrolledText(window, state="disable", padx=5, pady=5)
    text_widget.pack(pady=5, padx=5)

    entry_widget = tk.Entry(window)
    entry_widget.pack(padx=5, pady=5, fill=tk.BOTH, expand=1)
    entry_widget.bind(
        "<Return>",
        lambda event: send_message(
            event, client_socket, username, text_widget, entry_widget
        ),
    )

    # Bucle en escucha de nuevos mensajes
    thread = threading.Thread(target=receive_message, args=(client_socket, text_widget))
    thread.daemon = True
    thread.start()

    window.mainloop()
    client_socket.close()


if __name__ == "__main__":
    client_program()
