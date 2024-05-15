#!/usr/bin/env python3

""" Implementacion de sockets con python  """

import socket

# NOTE: Creando el server socket
# NOTE: socket.AF_iNET -> Familia ip (ipv4)
# NOTE: socket.SOCK_STREAM -> tipo se conexion (TCP)
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# INFO: Aqui estariamos definiendo por donde vamos a estar en escucha
server_address = ("localhost", 1234)
server_socket.bind(server_address)

# INFO: Limitar el límite de conexiones a 1
server_socket.listen(1)

while True:

    # NOTE: aceptando la conexion cliente servidor y viseversa
    client_socket, client_address = server_socket.accept()

    # datos recivibidos del cliente (.decode para convertir de bites a strings)
    data = client_socket.recv(1024)

    # NOTE: los mensajes deben ser decodificados al enviar o recibirse
    print(f"\n[+] Mensaje recibido del cliente: {data.decode()}")
    print(
        f"\n[+] Información del cliente que se ha comunicado con nosotros: {client_address}"
    )

    # NOTE: Respueta a la recepcion del mensaje del cliente
    client_socket.sendall(f"[+] Un salufo crack\n".encode())
    # NOTE: Cerrando la conexion con el cliente
    client_socket.close()
