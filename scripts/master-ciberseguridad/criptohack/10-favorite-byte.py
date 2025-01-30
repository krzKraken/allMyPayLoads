#!/usr/bin/env python3

from pwn import xor 

if __name__=='__main__':
    texto_cifrado = '73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d'
    text_bytes = bytes.fromhex(texto_cifrado)
    for d in range(256):
        texto_descifrado = xor(text_bytes, d)
        if b'crypto' in texto_descifrado:
            print(texto_descifrado)
            
