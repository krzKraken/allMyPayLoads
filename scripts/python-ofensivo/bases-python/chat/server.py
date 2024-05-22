import socket 
import threading

def server_program():
    HOST= 'localhost'
    PORT= 12345
    #Create socket 
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #Settings socket (reutilize ports)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind((HOST, PORT))
    server_socket.listen()
    print(f'[+] El servidor esta a la escucha del servidor por el puerto {PORT}')

    clients = []
    usernames={}

    while True:
        client_socket, address = server_socket.accept()
        clients.append(client_socket)
        print(f'[+] Se ha conectado un cliente {address}')


if __name__=='__main__':
    server_program()

