#!/usr/bin/env python3

# import os
import requests
from rich import print

# NOTE: Hacer una peticion get a google.com
response = requests.get("https://google.com")
print(f"\n[+] Estatus code: {response.status_code}")

# NOTE: mostrar el contenido de la peticion
with open("index.html", "w") as file:
    file.write(response.text)

# os.system("cat index.html")

# HACK: Utilizando la pagina https://httpbin/org/get

# NOTE: enviando peticion GET con varios parametros
params = {"key1": "value1", "key2": "value2", "key3": "value3"}

response = requests.get("https://httpbin.org/get", params=params)
print(response.text)

# NOTE: Enviando peticion POST

payloads = {"key1": "value1", "key2": "value2", "key3": "value3"}
response = requests.post("https://httpbin.org/post", params=params, data=payloads)
print(response.text)
