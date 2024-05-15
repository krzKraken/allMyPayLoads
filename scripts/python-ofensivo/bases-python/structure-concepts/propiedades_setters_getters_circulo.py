#!/usr/bin/env python3

""" Circulo properties """

from math import pi


class Circulo:
    def __init__(self, radio):
        self._radio = radio
        print(f"[+] Circulo creado! radio: {self._radio}")

    @property
    def radio(self):
        """radio property."""
        return self._radio

    @radio.setter
    def radio(self, value):
        self._radio = value

    @property
    def diametro(self):
        return self._radio * 2

    @property
    def area(self):
        return round(self._radio * pi, 2)


circulo = Circulo(100)
print(circulo.radio)
print(circulo.diametro)
print(circulo.area)
# Setter
circulo.radio = 10

print(circulo.radio)
print(circulo.diametro)
print(circulo.area)
