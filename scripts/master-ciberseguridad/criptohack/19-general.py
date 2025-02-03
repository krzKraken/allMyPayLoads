#!/usr/bin/env python3

import signal 
import requests 
import sys 
import subprocess
import os 
from bs4 import BeautifulSoup
from Crypto.PublicKey import RSA
import textwrap 



transparency_rsa = '''
30:82:01:22:30:0d:06:09:2a:86:48:86:f7:0d:01:01
:01:05:00:03:82:01:0f:00:30:82:01:0a:02:82:01:0
1:00:b9:88:f4:ea:6e:6a:e0:cf:12:b0:44:30:29:7f:
b9:34:fb:36:97:20:76:93:b8:1e:67:0e:2b:3f:af:1e
:51:99:aa:38:37:aa:c4:38:ef:e6:69:4b:63:69:f3:f
d:12:6c:3d:d9:2c:e0:9f:b2:e6:df:7a:28:0c:a8:dd:
2e:60:98:3a:84:38:c1:bb:26:0a:09:f4:a5:3e:e0:73
:d0:17:33:fd:0b:c1:b2:fa:18:ac:0a:17:68:f5:e1:7
a:51:e5:86:4e:2a:1a:cc:50:c8:75:15:0a:fa:06:66:
f3:57:35:88:f1:21:38:12:18:bb:70:9a:bb:7d:8b:46
:db:fe:2f:db:f3:aa:b7:b4:3a:59:5f:ee:87:87:a9:c
6:dc:30:12:0a:2f:a3:29:b0:93:06:fa:77:89:3e:72:
02:23:7e:81:65:91:0c:bb:ab:fa:7f:cc:c8:2a:e0:7b
:55:41:c0:6c:37:50:ea:db:01:cc:ba:57:cf:b5:cf:0
5:47:8a:3d:ad:45:93:c7:76:d8:42:3d:f6:97:87:c1:
6b:74:46:e2:4f:d1:0b:09:9e:c6:b8:a2:3e:82:ea:51
:3e:73:9f:af:54:76:ba:8d:5b:19:92:99:76:3e:e5:d
9:d3:96:ba:f7:13:91:67:8a:2a:fa:7c:33:2b:c3:bf:
4a:dd:61:6c:d0:57:b1:02:03:01:00:01
'''



def def_handler(sig, frame):
    print(f'\n\n[!] Saliendo...\n\n')
    sys.exit(1)

signal.signal(signal.SIGINT, def_handler)

def crear_directorio():

    directorio = 'certificados'

    try: 
        os.mkdir(directorio)
        print(f'\t[+] Directorio {directorio} creado con exito...\n')
    except FileExistsError:
        print(f'El directorio {directorio} ya existe')

def get_crt_ids():
    comando = "curl -s 'https://crt.sh/?q=cryptohack.org&dir=^&sort=1&group=none' | grep -oP '\\?id=\\K\\d+'"
    response = subprocess.run(comando, shell=True, capture_output=True, text=True)
    
    if response != None:
        print(f'\t[+] Ids capturados...\n')
    else:
        print(f'\t[-] No se lograron capturar ids de certificados')
    
    with open('./certificados/cert_ids.txt', 'w') as f:
        f.write(response.stdout)


def get_crt(id):
    url = f'https://crt.sh/?id={id}'
    response = requests.get(url)
    print(response.text)

def obtener_modulus(id):
    url = f'https://crt.sh/?id={id}'
    # Hacer la petición GET al sitio
    headers = {"User-Agent": "Mozilla/5.0"}  # Evitar bloqueos por bot
    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        print(f"Error: Código de estado {response.status_code}")
        return

    # Analizar HTML con BeautifulSoup
    soup = BeautifulSoup(response.text, "html.parser")

    # Buscar el texto que contiene "Modulus:"
    text_elements = soup.find_all("td", class_="text")

    for element in text_elements:
        if "Modulus:" in element.text:
            modulus_text = element.text.split("Modulus")[-1]
            modulus_lines = modulus_text.split("\n")  # Dividir en líneas
            modulus_cleaned = [line.strip() for line in modulus_lines if ":" in line]  # Filtrar líneas con ":"
            modulus = "".join(modulus_cleaned)  # Unir en una sola cadena
            return modulus

    return "Modulus no encontrado"
    
def pem_to_hex():
    with open('./transparency.pem', 'rb') as f:
        key = RSA.import_key(f.read())

        der_key = key.export_key(format="DER")
        hex_key = der_key.hex()

        formatted_hex = ':'.join(textwrap.wrap(hex_key, 2))
        hex_lines = textwrap.wrap(formatted_hex, 45)

        for line in hex_lines:
            print(line)

    

if __name__=='__main__':
    print(f'\n[+] Mi public key: ')
    pem_to_hex()
    print(f'\n[+] Creando directorio... certificados\n')
    crear_directorio()
    print(f'\n[+] Obteniendo ids certificados...\n')
    ids = get_crt_ids()
    print(f'\n[+] Obteniendo todos los certificados...\n')
    with open('./certificados/cert_ids.txt') as file:
        lista = file.readlines()
    lista = [line.strip() for line in lista]
    
    for i in lista:
        print(f'\n[+] output....\n\n')
        obtener_modulus(i)



