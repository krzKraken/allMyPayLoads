#!/usr/bin/env python3
""" Proyecto Animales """
from rich import print


class Animal:
    def __init__(self, nombre, especie):
        self.nombre = nombre
        self.especie = especie
        self.alimentado = False

    def __str__(self):
        return f"El {self.especie} {self.nombre} - ({self.alimentado})"

    def __repr__(self):
        return self.__str__()

    def alimentar(self):
        self.alimentado = True

    def vender(self):
        self.alimentado = False


class TiendaAnimales:
    def __init__(self, nombre):
        self.nombre = nombre
        self.animales = []

    def agregar_animal(self, animal):
        self.animales.append(animal)

    def mostrar_animales(self):
        print(self.animales)
        return [animal for animal in self.animales]

    def vender_animal(self, nombre):
        for animal in self.animales:
            if animal.nombre == nombre:
                print("[+] Animal existe")
                animal.vender()
                self.animales.remove(animal)
                return
        print(
            f"\n[!] No se ha encontrado ningun animal en la tienda con nombre {nombre}"
        )

    @property
    def alimentar_animales(self):
        for animal in self.animales:
            if not animal.alimentado:
                animal.alimentar()
                print(f"{animal.nombre} se alimento!")


if __name__ == "__main__":

    tienda = TiendaAnimales("Mi tienda de animales")

    gato = Animal("Tijuana", "Gato")
    perro = Animal("Juan", "Perro")
    camaleon = Animal("Marisol", "Camaleon")
    camaleon.alimentado = True

    tienda.agregar_animal(gato)
    tienda.agregar_animal(perro)
    tienda.agregar_animal(camaleon)

    tienda.mostrar_animales()
    tienda.alimentar_animales
    tienda.mostrar_animales()

    tienda.vender_animal("Tijuan")
    tienda.mostrar_animales()
