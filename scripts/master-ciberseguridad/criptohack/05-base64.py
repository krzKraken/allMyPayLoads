#!/usr/bin/env python3

import base64

encoded_text = '72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf'

if __name__=='__main__':
    from_hex_text = bytes.fromhex(encoded_text)
    print(from_hex_text)
    text = base64.b64encode(from_hex_text).decode()
    print(text)

