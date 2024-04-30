#!/usr/bin/env python3


class A:
    def __init__(self, valor):
        self.valor = valor
        print(f"El valor recibido en X es: {self.valor}")

    def saludo(self):
        """Metodo de class padre"""
        return "Saludo desde metodo de la clase padre A"


class B(A):

    def __init__(self, valor_x, valor_y):
        self.valor_y = valor_y
        super().__init__(valor_x)
        print(f"El valor recibiso en Y es: {self.valor_y}")

    def saludo(self):
        """Metodo de clase sobre escribe a la clase padre"""
        saludar = super().saludo()
        print(saludar, "Tambien desde la clase hija")


puntos = B(10, 20)
puntos.saludo()
