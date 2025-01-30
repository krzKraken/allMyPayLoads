#!/usr/bin/env python3

if __name__=='__main__':
    ascii = [99, 114, 121, 112, 116, 111, 123, 65, 83, 67, 73, 73, 95, 112, 114, 49, 110, 116, 52, 98, 108, 51, 125]
    texto_alfa = ""

    for c in ascii:
        texto_alfa += chr(c) 
    print(texto_alfa)
    
