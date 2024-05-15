# /usr/bin/env python3


import socket


def start_client():
    host = "localhost"
    port = 1234

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))
        text = input("[+] Escriba el texto al server: ")
        s.sendall(f"{text}".encode())
        data = s.recv(1024)

    print(f"[+] Informacion recibida del server al cliente {data.decode()}")


start_client()
