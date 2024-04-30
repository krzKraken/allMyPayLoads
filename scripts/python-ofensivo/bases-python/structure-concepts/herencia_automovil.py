#!/usr/bin/env python3
""" herencia y polimorfirmo """

from rich import print


# ? class vehiculo
class Vehiculo:
    def __init__(self, marca, modelo):
        """Class vehiculo"""

        self.marca = marca
        self.modelo = modelo

    def describir(self):
        """Descripcion de vehiculo"""
        return f"[+] El vehiculo es un {self.modelo} de marca {self.marca}"


class Carro(Vehiculo):
    def describir(self):
        return f"[!] El vehiculo es un carro: {self.modelo} de marca {self.marca}"


class Moto(Vehiculo):
    def describir(self):
        return f"[!] El vehiculo es una moto: {self.modelo} de marca {self.marca}"


# NOTE: Objetos herencia
my_carro = Vehiculo("Toyora", "Corolla")
print("[green] Herencia [/green]")
print(my_carro.describir())


print("[green] Polimorfismo [/green]")
my_carro_dos = Carro("Nissan", "Prado")
my_moto = Moto("Honda", "CRM")


# NOTE: Objetos polimorfismo
def descripcion_polimorfismo(objeto_vehiculo):
    """Funcion polimorfismo"""
    print(objeto_vehiculo.describir())


descripcion_polimorfismo(my_carro_dos)
descripcion_polimorfismo(my_moto)
