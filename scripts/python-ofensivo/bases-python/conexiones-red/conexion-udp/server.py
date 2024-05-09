#!/usr/bin/env python3

import socket

# NOTE: AF_INET -> familia ipv4
# NOTE: SOCK_DGRAM -> protocolo udp


def start_udp_server():
    """Function udp server conection"""
    host = "localhost"
    port = 1234

    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:

        s.bind((host, port))
        # INFO: UDP dont need .accept() or listen(1)

        # conn, addrs = s.accept()
        # s.listen(1)
        print(f"[+] Servidor arrancado en {host}:{port}\n")

        while True:

            data, addr = s.recvfrom(1024)
            if data:
                print("\n[+] Datos recibidos desde cliente: \n")
                print(f"Cliente: {data.decode()}")
                print(f"Cliente conectado por: {addr}")


start_udp_server()
