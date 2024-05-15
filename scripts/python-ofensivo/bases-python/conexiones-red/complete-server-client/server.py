#!/usr/bin/env python3

import socket


# Function start server
def start_server():
    host = "localhost"
    port = 1234

    # with open -> with sockets
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        # .bind recibe una tupla de host y port
        s.bind((host, port))
        print(f"[+] Server listening in:{host}:{port}\n")
        # NOTE: allowing client's connections
        s.listen(1)
        conn, addr = s.accept()

        # INFO: If a client connect with the server
        with conn:
            print(f"A client has connected to server: {addr}\n")
            while True:
                data = conn.recv(1024)
                if data.decode() == "hola":
                    print(f"[+] Datos recibidos del cliente: {data.decode()}")
                    conn.sendall(b"[+] Como estas?")
                elif data.decode():
                    print(f"[+] Datos recibidos del cliente: {data.decode()}")
                    conn.sendall(f"[+] {data}".encode())
                if not data:
                    break


start_server()
