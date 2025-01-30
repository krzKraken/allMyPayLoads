#!/usr/bin/env python3

from pwn import xor 

KEY1 = 'a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313'
KEY2_KEY1 = '37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e'
KEY2_KEY3 = 'c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1'
FLAG_KEY1_KEY3_KEY2 = '04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf'
b_k1 = bytes.fromhex(KEY1)
b_k2_k1=bytes.fromhex(KEY2_KEY1)
b_k2_k3=bytes.fromhex(KEY2_KEY3)
b_f_k1_k2_k3=bytes.fromhex(FLAG_KEY1_KEY3_KEY2)
if __name__=='__main__':
    k2 = xor(b_k2_k1, b_k1)
    k3 = xor(b_k2_k3, k2)
    flag = xor(b_f_k1_k2_k3, b_k1, k2, k3).decode()
    print(flag)
