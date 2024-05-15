#!/usr/bin/env python3

import multiprocessing
import threading
import time

import requests

domains = [
    "https://google.com",
    "https://facebook.com",
    "https://twitch.com",
    "https://yahoo.com",
]

# NOTE: Script SIN hilos
print(f"\n---------[+] Corriendo script sin hilos---------")
start_time = time.time()

for url in domains:
    response = requests.get(url)
    print(f"\n[+] URL [{url} : {len(response.text)} bytes]")

end_time = time.time()

print(f"\nTiempo transcurrido sin threading: {round(end_time - start_time, 2)} seconds")


# NOTE: Script CON hilos
print(f"\n----------[+] Corriendo script con hilos")


def get_time_url(domain_list):
    response = requests.get(url)
    print(f"\n[+] URL [{url} : {len(response.content)} bytes]")


start_time = time.time()
hilos = []

# NOTE: Ejecuta los hilos
for url in domains:
    hilo = threading.Thread(target=get_time_url, args=(url,))
    hilo.start()
    hilos.append(hilo)

# NOTE: Espera a que todos los hilos terminen
for hilo in hilos:
    hilo.join()

end_time = time.time()

print(f"\n[+] tiempo transcurrido con threading: {round(end_time - start_time, 2)}")


print(f"\n----------[+] Ejecutando script con multiprocessing----------- ")


def realizar_peticion(url):
    response = requests.get(url)
    print(f"\n[+] URL [{url} : {len(response.content)} bytes]")


start_time = time.time()

process = []

for url in domains:
    proceso = multiprocessing.Process(target=realizar_peticion, args=(url,))
    proceso.start()
    process.append(proceso)

for process in process:
    process.join()

end_time = time.time()
print(
    f"\n[+] Tiempo total transcurrido con multiprocessing: {round(end_time - start_time, 2)} segundos"
)
