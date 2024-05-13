#!/usr/bin/env python3

import requests
from rich import print

url = "https://httpbin.org/cookies"
set_cookies_url = "https://httpbin.org/cookies/set/nombre/valor123"


# INFO: Se crean las cookies de sesion pero no las arrastra
print("\n[+] Creando una cookie\n")
response = requests.get(set_cookies_url)
print(response.text)
print(f"\n[+] Consultando las cookies a {url}\n")
response = requests.get(url)
print(response.text)

# INFO: Para arrastrar una cookie de sesion podemos crear una sesion requests.sesion()
print("\n[+] Creando una requests.Session()\n")
s = requests.Session()
print("\n[+] Sesion creada \n")

data = s.get(set_cookies_url)
print(f"Data: {data.text}")

print("[+] Imprimiendo las cookies de sessin")
data = s.get(url)
print(f"DATA: {data.text}")
