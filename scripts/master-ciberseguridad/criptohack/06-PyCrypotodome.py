#!/usr/bin/env python3

from Crypto.Util.number import bytes_to_long, long_to_bytes 

texto_encriptado = 11515195063862318899931685488813747395775516287289682636499965282714637259206269


if __name__=='__main__':
    text = long_to_bytes(texto_encriptado)
    print(text.decode())
