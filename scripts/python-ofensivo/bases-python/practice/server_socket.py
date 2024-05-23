import socket

def server_program():
    port = 12345
    host = 'localhost'
    print(f"[+] Server running on http://{host}:{port}")
    
    # Server settings
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind((host, port))
    server_socket.listen()

    while True:
        # while a new connection is stablished
        client_socket, client_address = server_socket.accept()
        print(f'Se ha conectado: \n{client_socket}\nEn el puerto: {client_address}')
        recibeDeCliente = client_socket.recv(1024)
        print(f'Se recibe del cliente: {recibeDeCliente}')
        
        client_socket.sendall('hola desde el server_socket'.encode())


if __name__ == '__main__':
    server_program()
