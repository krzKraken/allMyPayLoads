#!/usr/bin/env python3

import math


class Circunferencia:
    def __init__(self, radio):
        self._radio = radio
        print(f"Circulo creado, radio {self._radio}")

    @property
    def radio(self):
        return f"radio: {self._radio}"

    @radio.setter
    def radio(self, value):
        self._radio = value
        return f"radio: {self._radio}"

    @property
    def diametro(self):
        return f"diametro: {self._radio*2}"

    @property
    def area(self):
        return f"Area: {round(self._radio * math.pi,2)}"


circulo = Circunferencia(10)
print(circulo.radio)
print(circulo.diametro)
print(circulo.area)
