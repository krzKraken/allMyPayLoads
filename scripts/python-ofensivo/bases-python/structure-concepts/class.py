#!/usr/bin/env python3
"""
Ejercicios con clases
"""
from rich import print


class Persona(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def saludo(self):
        """hola"""
        # NOTE:
        # print(f"Hola, soy {self.name} y tengo {self.age}")
        return f"Hola, soy {self.name} y tengo {self.age}"


cris = Persona("kris", 33)
print(cris.saludo())
