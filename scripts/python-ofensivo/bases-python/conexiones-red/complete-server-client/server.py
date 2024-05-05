#!/usr/bin/env python3

import socket


# Function start server
def start_server():
    host = "localhost"
    port = 4444

    # with open -> with sockets
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        # .bind recibe una tupla de host y port
        s.bind((host, port))
        print(f"[+] Server listening in:{host}:{port}")
        # NOTE: allowing client's connections
        conn, addr = s.accept()

        # INFO: If a client connect with the server
        with conn:
            print(f"A client has connected to server: {addr}")
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                conn.sendall(data)


start_server()
