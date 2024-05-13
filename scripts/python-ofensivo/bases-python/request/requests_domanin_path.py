#!/usr/bin/env python3

import requests

url = "http://github.com"

# NOTE: not allow automatic redirect
response = requests.get(url, allow_redirects=False)
print(f"[+] La url a la que apuntamos es: { response.url }")

# NOTE: Allowing and capture the path on subdomanins
response = requests.get(url)

# INFO: All the routrace in the requests is stored on requests.hist
for request in response.history:
    print(
        f"[+] Pasamos por {request.url} con un codigo de estado: {request.status_code}"
    )
print(
    f"[+] Finalmente terminamso en {response.url} con un codigo de estado: {response.status_code}"
)
