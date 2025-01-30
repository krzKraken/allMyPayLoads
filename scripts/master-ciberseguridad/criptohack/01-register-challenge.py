#!/usr/bin/env python3

if __name__ == '__main__':
    texto_cifrado = "QZPADEQ MPHMZOQ OQZEGE ADBTMZ"

    for desplazamiento in range(1, 27):
        texto_descifrado = ""
        
        for c in texto_cifrado:
            if c.isalpha():  # Solo procesa letras
                base = ord('A') if c.isupper() else ord('a')
                nuevo_caracter = chr((ord(c) - base - desplazamiento) % 26 + base)
                texto_descifrado += nuevo_caracter
            else:
                texto_descifrado += c  # Mantiene espacios y otros caracteres

        print(f"Desplazamiento {desplazamiento}: {texto_descifrado}")


