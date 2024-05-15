#!/usr/bin/env python3

import socket


def start_chat_client():
    host = "localhost"
    port = 1234

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Conectando al server

    client_socket.connect((host, port))

    while True:
        client_message = input(f"\n[+] Message to server: ")
        client_socket.send(client_message.encode())
        if client_message == "bye":
            break
        server_message = client_socket.recv(1024).strip().decode()
        print(f"[+] Message from the server: {server_message}")
    client_socket.close()


start_chat_client()
