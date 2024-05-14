#!/usr/bin/env python3

""" urllib3 USE """

import json

import urllib3

print("\n[+]Get request\n")
http = urllib3.PoolManager()  # Controladoe de conexiones
url = "https://httpbin.org/get"
response = http.request("GET", url)
print(response.data.decode())

print("\n[+] Post request\n")

url = "https://httpbin.org/post"
data = {"atributo": "valor"}
encoded_data = json.dumps(data).encode()
response = http.request("POST", url, body=encoded_data)
print(response.data.decode())
