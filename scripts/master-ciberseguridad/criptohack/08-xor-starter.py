#!/usr/bin/env python3

from pwn import xor 

if __name__=='__main__':

    label = b'label'
    text = ''
    for c in label:
        text += xor(c, 13).decode()
        print(text)
    print(f"cryto{{{text}}}")
def xor_string(label, key=13):
    return ''.join(chr(ord(c) ^ key) for c in label)

# Prueba con una cadena de ejemplo
label = "label"
new_string = xor_string(label)
flag = f"crypto{{{new_string}}}"

print(flag)
