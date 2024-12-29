#!/usr/bin/env python3

import socket
import threading
import tkinter as tk
from tkinter.scrolledtext import ScrolledText


def exit_request(client_socket, username, window):
    client_socket.sendall(f"[!] El usuario {username} ha abandonado el chat\n".encode())

    client_socket.close()
    window.quit()
    window.destroy()


def list_users_request(client_socket):
    client_socket.sendall("!usuarios".encode())


def send_message(event, client_socket, username, text_widget, entry_widget):
    print("\n[+] Se ha presionado la tecla enter")
    message = entry_widget.get()
    print(f"\n[+] El usuario {username}, ha escrito: {message}")
    client_socket.sendall(f"{username} > {message}".encode())
    entry_widget.delete(0, tk.END)
    text_widget.configure(state="normal")
    text_widget.insert(tk.END, f"{username} > {message}\n")
    text_widget.configure(state="disable")
    text_widget.yview_moveto(1.0)


def receive_message(client_socket, text_widget):
    while True:
        try:
            message = client_socket.recv(1024).decode()

            if not message:
                break
            text_widget.configure(state="normal")
            text_widget.insert(tk.END, message)
            text_widget.configure(state="disable")
            text_widget.yview_moveto(1.0)
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
    window.geometry("600x600")
    window.attributes("-topmost", True)
    window.title("Chat")
    # NOTE: State disable desabilita la escritura
    text_widget = ScrolledText(window, state="disable", padx=5, pady=5)
    text_widget.pack(pady=5, padx=5)

    frame_widget = tk.Frame(window, bg="#442233")
    frame_widget.pack(fill=tk.BOTH, expand=1, padx=5, pady=5)

    entry_widget = tk.Entry(frame_widget)
    entry_widget.pack(fill=tk.BOTH, expand=1, side=tk.LEFT, pady=5, padx=5)
    entry_widget.bind(
        "<Return>",
        lambda event: send_message(
            event, client_socket, username, text_widget, entry_widget
        ),
    )

    button_widget = tk.Button(
        frame_widget,
        text="Enviar",
        command=lambda: send_message(
            None, client_socket, username, text_widget, entry_widget
        ),
    )
    button_widget.pack(side=tk.RIGHT, padx=5)

    users_widget = tk.Button(
        window,
        text="Listar Usuarios",
        command=lambda: list_users_request(client_socket),
    )
    users_widget.pack(
        side=tk.BOTTOM,
    )

    exit_widget = tk.Button(
        window,
        text="Salir",
        command=lambda: exit_request(client_socket, username, window),
    )
    exit_widget.pack(
        side=tk.BOTTOM,
    )

    # Bucle en escucha de nuevos mensajes
    thread = threading.Thread(target=receive_message, args=(client_socket, text_widget))
    thread.daemon = True
    thread.start()

    window.mainloop()
    client_socket.close()


if __name__ == "__main__":
    client_program()
