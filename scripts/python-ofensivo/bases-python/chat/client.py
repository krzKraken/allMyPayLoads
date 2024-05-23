import socket


def client_program():
    HOST='localhost'
    PORT=12345

    #NOTE: Create the client socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #NOTE: Connect the client to host, port
    client_socket.connect((HOST, PORT))

    username= input('\n[+] Introduce tu usuario')
    #NOTE: Enviando info del cliente a server
    client_socket.sendall(username.encode())
    

if __name__ == '__main__':
    client_program()
