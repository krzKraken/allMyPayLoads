#!/usr/bin/env python3

""" urllib3 USE """

import json
from enum import verify
from ssl import CERT_REQUIRED

import urllib3

# NOTE: Get requests
print("\n----------[+]Get request-------------\n")
http = urllib3.PoolManager()  # Controladoe de conexiones
url = "https://httpbin.org/get"
response = http.request("GET", url)
print(response.data.decode())


# NOTE: Post requests
print("\n----------[+] Post request----------\n")
http = urllib3.PoolManager()  # Controladoe de conexiones
url = "https://httpbin.org/post"
data = {"atributo": "valor"}
encoded_data = json.dumps(data).encode()
response = http.request("POST", url, body=encoded_data)
print(response.data.decode())

# NOTE: Arrastrando headers
print("\n----------[+] Post with headers----------\n")
http = urllib3.PoolManager()  # Controladoe de conexiones
url = "https://httpbin.org/post"
data = {"atributo": "valor"}
headers = {"Content-Type": "application/json"}
encoded_data = json.dumps(data).encode()

response = http.request("POST", url, body=encoded_data, headers=headers)
print(response.data.decode())

# NOTE: Creando nueva cabecera
print("\n-------[+] Creando nuevo headers-----------\n")
http = urllib3.PoolManager()
url = "https://httpbin.org/get"
headers = {"myNuevaCabecera": "ValorCabecera"}

response = http.request("GET", url, headers=headers)
print(response.data.decode())

# NOTE: sin redirect
print("\n-------------[+] Solocititud sin redirect--------------\n")
http = urllib3.PoolManager()
url = "https://httpbin.org/redirect/1"
response = http.request(method="GET", url=url, redirect=False)
print(response.data.decode())
print("Status code: ", response.status)

# NOTE:
print("\n------------[+] Get redirect location------\n")
print(response.get_redirect_location())


# NOTE: Alguna https con certificado autofirmado
print("\n-----------[+] Certificados autofirmados----------\n")
url = "https://13.109.185.30/"

# HACK: Ignorar el autofirmado
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

http = urllib3.PoolManager(cert_reqs="CERT_NONE")  # Controlador de conexiones
request = http.request("GET", url)
print(response.data.decode())
