#!/usr/bin/env python3

from rich import print


class Animal:
    def __init__(self, nombre):
        self.nombre = nombre

    def hablar(self):
        raise NotImplementedError(
            "Esta subclase debe ser definida en la implementacion del metodo"
        )


class Gato(Animal):

    def hablar(self):
        return "Soy un gato!"


class Perro(Animal):

    def hablar(self):
        return "Soy un perro!"


#! Esto es polimorfismo
def hacer_hablar(obj):
    """Polimorfismo"""
    print(
        f"""Esto es polimorfismo, estoy llamando al metodo hablar de la clase Gato que hereda de Animal: {obj.hablar()}"""
    )


gato = Gato("Don gato")
print(gato.hablar())

hacer_hablar(gato)
