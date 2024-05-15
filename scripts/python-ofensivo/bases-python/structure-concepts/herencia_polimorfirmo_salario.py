#!/usr/bin/env python3


class Persona:

    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def saludo(self):
        return f"Me llamo {self.nombre} tengo {self.edad} años"


class Empleado(Persona):

    def __init__(self, nombre, edad, salario):
        super().__init__(nombre, edad)
        self.salario = salario

    def saludo(self):

        return f"{super().saludo()}, y cobro {self.salario} euro brutos anuales"


persona = Empleado("Joss", 23, 5000)
print(persona.saludo())
