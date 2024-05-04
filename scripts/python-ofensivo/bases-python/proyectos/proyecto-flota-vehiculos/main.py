#!/usr/bin/env python3

from rich import print


class Vehiculo:
    def __init__(self, matricula, modelo):
        self.matricula = matricula
        self.modelo = modelo
        self.disponible = True

    def __str__(self):
        return f"Vehiculo( matricula = {self.matricula}, modelo={self.modelo}, disponible={self.disponible}"

    # def __repr__(self):
    # return self.__str__()
    def alquilar(self):
        if self.disponible:
            self.disponible = False
        else:
            print("[red][!][/red] El vehiculo no se encuentra disponible")

    def devolver(self):
        if not self.disponible:
            self.disponible = True
        else:
            print("[red][!][/red] El vehiculo ya habia sido devuelto")


class Flota:
    def __init__(self):
        self.vehiculos = []

    def agregar_vehiculo(self, vehiculo):
        self.vehiculos.append(vehiculo)

    def __str__(self):
        return "\n".join(str(vehiculo) for vehiculo in self.vehiculos)

    def alquilar_vehiculo(self, matricula):
        for vehiculo in self.vehiculos:
            if vehiculo.matricula == matricula:
                vehiculo.alquilar()
                return

    def devolver_vehiculo(self, matricula):
        for vehiculo in self.vehiculos:
            if vehiculo.matricula == matricula:
                vehiculo.devolver()
                return


if __name__ == "__main__":
    flota = Flota()

    flota.agregar_vehiculo(Vehiculo("BAS123", "Toyota Corolla"))
    flota.agregar_vehiculo(Vehiculo("MJH123", "Chevrolet Camaro"))
    print("\n[+] Flota inicial: \n")
    print(flota, "\n")

    flota.alquilar_vehiculo("BAS123")

    print("Flota despues de alquilar BAS123")
    print(flota, "\n")

    print("flota despues de devolver BAS123")
    flota.devolver_vehiculo("BAS123")
    print(flota)
