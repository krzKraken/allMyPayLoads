#!/usr/bin/env python3

import socket


def start_udp_client():
    """Client udp conection"""
    host = "localhost"
    port = 1234

    while True:
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
            message = input("write message to the server: ").encode("utf-8")
            s.sendto(message, (host, port))
            print(f"[+] Client udp conection by {host}:{port}")
            if message.strip() == "bye":
                break


start_udp_client()
