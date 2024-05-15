#!/usr/bin/env python3

from pwn import log

try:
    value = 1 / 0
except ZeroDivisionError:
    print("Error! hola!")
