#!/usr/bin/env python3

import requests
from requests.auth import HTTPBasicAuth

# INFO: using https://httpbin.org/basic-auth/foo/bar

url = "https://httpbin.org/basic-auth/foo/bar"

# NOTE: Forma facil
print("[+] Basic auth - metodo facil")
response = requests.get(url, auth=("foo", "bar"))
print(f"data: {response.text}")

# NOTE: Otro metodo de autenticacion

from requests.auth import HTTPBasicAuth

response = requests.get(url, auth=HTTPBasicAuth("foo", "bar"))
print("[+] Basic auth class - Metodo de clase")
print(f"data: {response.text}")
