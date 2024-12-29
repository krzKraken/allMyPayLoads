#!/usr/bin/env python3

"""
Este script automatiza la encriptacion de un documento 'testamento.txt en AES256, esta clave generada se fragmenta en 3 y es encriptada con la clave pública de cada hermano y obtienen cada uno la clave priada y el fragmento encriptado con su respectiva clave pública. """

from termcolor import colored
import signal 
import sys 
import os 
from Crypto.Cipher import AES, PKCS1_OAEP
from Crypto.Util.Padding import pad, unpad
from Crypto.PublicKey import RSA


# Cntrl + c => Forzar salida 
def def_handler(sig, frame):
    print(colored('\nSaliendo...\n', 'red'))
    sys.exit(1)

signal.signal(signal.SIGINT, def_handler)

# LLave randomica de 32 bytes (256 bits) para AES256
def encriptacion_aes(documento, llave):
    # Leyendo el documento 
    with open(documento, 'rb') as doc:
        document_text = doc.read()

    # NOTE: Ajustando el tamaño del bloque para 16 bytes que requiere AES 
    data_en_bloques_AES = pad(document_text, AES.block_size)

    # Generando vector de inicializacion 
    iv = os.urandom(16) 
    
    # Cifrador AES en modo CBC
    cifrador = AES.new(llave, AES.MODE_CBC, iv)

    # Encriptando los datos 
    texto_cifrado = cifrador.encrypt(data_en_bloques_AES)

    # Creando el testamento cifrado 
    with open('testamento_encriptado'+'.enc', 'wb') as encrypted_file:
        encrypted_file.write(iv + texto_cifrado)
    print(colored(f'\n[+] Texto Original:\n\n{document_text.decode('utf-8')}', 'blue'))

    print(colored(f'[+] Texto cifrado con AES256 exito:\n', 'blue'))
    print(colored(f'{texto_cifrado.hex()}', 'blue'))
    print(colored(f'\n[!] LLave utilizada para encriptar:  {llave_secreta.hex()}\n', 'red'))


def split_key(key):
    # Dividir la clave AES en 3 partes iguales
    part_size = len(key) // 3
    return key[:part_size], key[part_size:2 * part_size], key[2 * part_size:]

def generador_claves_rsa(id):
    llave = RSA.generate(2048)
    clave_privada = llave.export_key()
    clave_publica = llave.public_key().export_key()
    with open(f'./llaves/h{id}/llave_priv_h{id}', 'wb') as f:
        f.write(clave_privada)
    print(colored(f'[+] Llave publica h{id}:\n{clave_publica}\n\nllave privada h{id}:\n {"*"*20}\n\n', 'yellow'))
    return clave_privada, clave_publica

def encriptar_con_rsa(clave_publica, data, id):
    rsa_key = RSA.import_key(clave_publica)
    cifrador = PKCS1_OAEP.new(rsa_key)
    dato_encriptado = cifrador.encrypt(data)
    with open(f'./llaves/h{id}/fragmento_h{id}.enc', 'wb') as f:
        f.write(dato_encriptado)
    return dato_encriptado

def desencriptador_con_rsa(ruta_clave_privada, ruta_dato_encriptado):
    with open(ruta_clave_privada, 'rb') as f:
        clave_privada = RSA.import_key(f.read())
    
    with open(ruta_dato_encriptado, 'rb') as f:
        dato_encriptado = f.read()

    cifrador = PKCS1_OAEP.new(clave_privada)

    dato_desencriptado = cifrador.decrypt(dato_encriptado)
    return dato_desencriptado


def desencriptacion_aes(documento_encriptado,llave_aes):
    
    with open(documento_encriptado, 'rb') as enc_doc:
        # obtenemos el iv de los 16 primeros bytes
        iv = enc_doc.read(16)
        texto_encriptado = enc_doc.read()
    
    # Creamos el decifrador AES en modo CBC 
    cifrador = AES.new(llave_aes, AES.MODE_CBC, iv)

    # Decifrar los datos
    texto_decifrado = cifrador.decrypt(texto_encriptado)
    texto_decifrado_sin_padding = unpad(texto_decifrado, AES.block_size)

    # Guardando el archivo desencriptado
    with open('testamento_desencriptado.txt', 'wb') as doc:
        doc.write(texto_decifrado_sin_padding)
    print(colored(f'\n[+] Documento desencriptado con exito\n'))

    print(colored(f'Contenido del testamento:\n{texto_decifrado_sin_padding.decode('utf-8')}', 'red'))

if __name__=='__main__':
    # Creamos el directorio de almacenamiento de las llaves 
    llaves_directorio = './llaves/'
    if not os.path.isdir(llaves_directorio):
        os.mkdir('llaves')
        os.mkdir('llaves/h1')
        os.mkdir('llaves/h2')
        os.mkdir('llaves/h3')
    # Generamos una llave dandom en bytes para encriptar con AES256
    llave_secreta = os.urandom(32)
    # with open('./llaves/llave_aes_testamento', 'wb') as doc:
        # doc.write(llave_secreta)


    encriptacion_aes('./testamento.txt', llave_secreta)
    # Dividimos la clave
    part1, part2, part3 = split_key(llave_secreta)
    print(f"Parte 1: {part1.hex()}")
    print(f"Parte 2: {part2.hex()}")
    print(f"Parte 3: {part3.hex()}")

    print(colored(f'[+] Generando Claves privadas y publicas para cada hijo\n', 'blue'))
    h1_priv, h1_pub = generador_claves_rsa(1)
    h2_priv, h2_pub = generador_claves_rsa(2)
    h3_priv, h3_pub = generador_claves_rsa(3)
    
    part1_h1_enc = encriptar_con_rsa(h1_pub, part1, 1)
    part2_h2_enc = encriptar_con_rsa(h2_pub, part2, 2)
    part3_h3_enc = encriptar_con_rsa(h3_pub, part3, 3)
    
    
    print(colored(f'[+] Fragmentos encriptados para cada hijo con su respectiva clave publica ', 'green'))
    print(colored(f'[+] Fragmento 1 de Hijo 1 encriptado con clave publica de Hijo 1:','blue'))
    print(part1_h1_enc.hex()+'\n')
    print(colored(f'[+] Fragmento 2 de Hijo 2 encriptado con clave publica de Hijo 2:','blue'))
    print(part2_h2_enc.hex()+'\n')
    print(colored(f'[+] Fragmento 3 de Hijo 3 encriptado con clave publica de Hijo 3:','blue'))
    print(part3_h3_enc.hex()+'\n')
    

    print(colored(f'[+] Los hermanos se ponen de acuerdo para leer el testamento y cada uno provee su clave privada para desencriptar y juntar los fragmentos'))
    llave_completa = desencriptador_con_rsa('./llaves/h1/llave_priv_h1', './llaves/h1/fragmento_h1.enc') + desencriptador_con_rsa('./llaves/h2/llave_priv_h2', './llaves/h2/fragmento_h2.enc') + desencriptador_con_rsa('./llaves/h3/llave_priv_h3','./llaves/h3/fragmento_h3.enc')
    print(colored(f'[+] llave completa desencriptada: {llave_completa.hex()}', 'yellow'))

    desencriptacion_aes('./testamento_encriptado.enc', llave_completa)
