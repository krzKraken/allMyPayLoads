#!/usr/bin/env python3

import socket

# NOTE: Creamos el socket (siempre lo mismo)
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_address = ("localhost", 1234)
# NOTE: para server es .bind para cliente es .connect
client_socket.connect(client_address)

# NOTE: Como cliente ya no limitamos numero de conexiones
# client_socket.listen(1)

try:
    mensaje = (
        f"[+] Este es el mensaje de prueba enviado desde el cliente al servidor..."
    )
    client_socket.sendall(mensaje.encode())
    data = client_socket.recv(1024)
    print(f"[+] El servidor nos ha respondido con este mensaje: {data.decode()}")
finally:
    client_socket.close()
