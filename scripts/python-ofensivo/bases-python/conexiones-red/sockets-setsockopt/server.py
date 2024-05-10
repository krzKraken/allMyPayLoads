#!/usr/bin/env python3

""" Editando las propiedades de los sockets (Por niveles) """

# debug in python
# import pdb
import socket
import threading

from rich import print


class ClientThread(threading.Thread):
    def __init__(self, client_sock, client_addr):
        super().__init__()
        self.client_sock = client_sock
        self.client_addr = client_addr

        print(
            f"[red][+] SERVER [/red] Nuevo cliente conectado por hilos: {client_addr}"
        )

    # INFO: Sobreescribomos el metodo run() del theading
    def run(self):
        message = ""

        while True:
            data = self.client_sock.recv(1024)
            message = data.decode()

            # pdb.set_trace()  #HACK: -> break point
            if message.strip() == "bye":
                break
            print(
                f"[green][+] CLIENT [/green] Mensaje enviado por el cliente:[green] {message}[/green]"
            )
            self.client_sock.send(
                f"[+] SERVER  Respuesta del server: {message}".encode("utf-8")
            )
        print(f"[red][+] SERVER [/red] Cliente {self.client_addr} Desconecado..!")
        self.client_sock.close()


def start_server():
    host = "localhost"
    port = 1234

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        # NOTE: setsockopt(nivel, propiedad , valor a setear)
        # INFO: socket.IPPROTO_TCP -> propiedades tcp
        # INFO: socket.SO_REUSEADDR -> propiedades puertos
        # INFO: socket.IPPROTO_IP  -> propiedades ipv4
        # INFO: socket.IPPROTO_UDP -> propiedades udp

        # HACK:  para que el puerto no quede en time_wait, se puede reutilizar despues de cerrar
        server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        # Server en escucha
        server_socket.bind((host, port))
        print("\n[+] Server en escucha de conexiones entrantes....\n")

        while True:
            # NOTE: no necesitamos especificar el numero de conexiones para multiples conexiones
            server_socket.listen()
            client_sock, client_addr = server_socket.accept()
            new_thread = ClientThread(client_sock, client_addr)
            new_thread.start()  # Run method()


start_server()
