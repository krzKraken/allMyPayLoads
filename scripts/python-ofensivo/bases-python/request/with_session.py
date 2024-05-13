#!/usr/bin/env python3

import requests

url = "https://httpbin.org/basic-auth/foo/bar"
with requests.Session() as session:
    session.auth = ("foo", "bar")
    response1 = session.get(url)
    print(f"[+] Autenticando con session: \n{response1.text}")

    response2 = session.get(url)
    print(f"[+] Autenticando con sesion \n{response2.text}")


response2 = requests.get(url)
print(f"[+] Autenticando sin sesion \n{response2.text}")
