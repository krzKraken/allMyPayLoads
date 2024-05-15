#!/usr/bin/env python3


class Punto:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, otro):
        # NOTE: Definir la suma de la clase
        """Este metodo especial define la suma de dos objetos punto"""
        x = self.x + otro.x
        y = self.y + otro.y
        return Punto(x, y)

    def __str__(self):
        return f"{self.x, self.y}"


punto1 = Punto(1, 3)
punto2 = Punto(3, 1)

print(punto1 + punto2)
