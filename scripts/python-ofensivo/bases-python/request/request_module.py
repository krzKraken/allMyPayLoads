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

# NOTE: Enviando headers personalizados

params = {"key1": "value1", "key2": "value2"}
headers = {"User-Agent": "my-app/0.1.0"}
response = requests.post("https://httpbin.org/post", params=params, headers=headers)
print(response.text)

# NOTE: Enviando headers personalizados por get
headers = {"User-Agent": "header-personalizado"}
response = requests.get("https://google.com", headers=headers)
print("\n[+] Enviando headers personalizados\n")
print(response.request.headers)


# NOTE: Utilizando excepciones en caso de error response.raise_for_status
print("\n[+] Try catch error time out\n")
timeout = 1
try:
    response = requests.get("https://google.com", timeout=timeout)
    response.raise_for_status()
except requests.Timeout:
    print(f"[!] Se ha excedido el tiempo de espera en la solicitud timeout:{timeout}")

except requests.HTTPError as http_err:
    print(f"[!] HTTP ERROR: {http_err}")
except requests.RequestException as err:
    print(f"[!] ERROR: {err}")

else:
    print(f"[+] No ha habido ningun error en la solicitud {response.status_code}")


# NOTE: Convirtiendo output en formato json data=json(requests)
print("\n[+] Output en response.json()")
data = requests.get("https://httpbin.org/get")
data = data.json()
if "headers" in data and "User-Agent" in data["headers"]:
    print(data["headers"]["User-Agent"])
else:
    print("[!] No se encontro campo en json()")
