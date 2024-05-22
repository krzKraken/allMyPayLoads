import socket
import threading


def server_program():

    HOST = "localhost"
    PORT = 12345

    # NOTE: Create server socket IPV4 family
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # NOTE: SetSocketOpt -> reuse ports
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    # NOTE: Socket en host y port
    server_socket.bind((HOST, PORT))
    # NOTE: Socket en escucha de n conexiones
    server_socket.listen()

    print(f"[+] Server runing on {HOST}:{PORT} waiting for conections...")

    # INFO: What's server do on any confirmed conection
    clients = []
    usernames = {}

    while True:

        client_socket, client_address = server_socket.accept()
        clients.append(client_socket)
        print(f"[+] Client has connected: \n\t { client_socket } \n\t {client_address}")


if __name__ == "__main__":
    server_program()
