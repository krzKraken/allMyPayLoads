#!/usr/bin/env python3

import socket


def start_udp_client():
    """Client udp conection"""
    host = "localhost"
    port = 1234

    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        mensaje = input("Escriba el mensaje al servidor ").encode("utf-8")
        s.sendto(mensaje, (host, port))
        print(f"[+] Client udp conection by {host}:{port}")


start_udp_client()
