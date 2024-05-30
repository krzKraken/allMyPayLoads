import socket 
import threading 

def server_program():
  host = 'localhost'
  port = 12345
  
  # crea el server socket
  server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  # Time wait no se ponga el servidor ocupado
  server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
  # En escucha en el puerto en el host
  server_socket.bind((host, port))
  # En escucha el server
  server_socket.listen()
  
  print(f'[+] El servidor esta en escucha en {host}:{port}')
  
  clients=[]
  # socket : username
  usernames={}
  
  
  while True:
    # Aceptando conexiones entrantes en el server
    client_socket, client_address=server_socket.accept()
    clients.append(client_socket)
    print(f'[+] Se ha conectado un nuevo cliente {client_address}')
    
    
    
  
  
  
  
  

if __name__ == '__main__':
  server_program()