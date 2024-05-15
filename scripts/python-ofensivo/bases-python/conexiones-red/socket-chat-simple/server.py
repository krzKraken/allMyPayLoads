#!/usr/bin/env python3


import socket

from rich import print


def start_chat_server():

    host = "localhost"
    port = 1234
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.setsockopt(
            socket.SOL_SOCKET, socket.SO_REUSEADDR, 1
        )  # Elimina el TIME_WAIT
        server_socket.bind((host, port))
        server_socket.listen(1)

        print("\n[yellow][SERVER][/yellow] Server waiting for one conection...")

        client_sock, client_addr = server_socket.accept()
        print(
            f"[yellow][SERVER][/yellow] A client has conected to the server: ({client_addr})"
        )

        while True:
            client_message = client_sock.recv(1024).decode().strip()
            print(f"[green][Client][/green] {client_message}")
            if client_message == "bye":
                break

            server_message = input("[SERVER] Mensaje para cliente:  ")
            client_sock.send(server_message.encode())
        client_sock.close()


start_chat_server()
