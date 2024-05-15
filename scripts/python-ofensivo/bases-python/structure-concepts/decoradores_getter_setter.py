#!/usr/bin/env python3


class Persona:
    def __init__(self, nombre, edad):
        self._nombre = nombre
        self._edad = edad

    @property
    def edad(self):  # Getter Edad
        return self._edad

    @edad.setter  # setter
    def edad(self, valor):
        if valor > 0:
            self._edad = valor
        else:
            raise ValueError("[!] No se aceptan edades igual o menores a 0")


manolo = Persona("manolo", 19)
# NOTE: Se accede a la variable protegida desde la propiedad
print(manolo.edad)

# NOTE: Se cambia el valor de la variable protegida  desde la propiedad
manolo.edad = 100
print(manolo.edad)
