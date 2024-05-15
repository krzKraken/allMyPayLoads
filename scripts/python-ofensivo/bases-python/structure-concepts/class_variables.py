#!/usr/bin/env python3


class Estudiantes:

    estudiantes = []

    def __init__(self, nombre, edad):

        self.nombre = nombre
        self.edad = edad

        Estudiantes.estudiantes.append(self)

    def __str__(self):

        return f"Class Estudiantes, {self.nombre} {self.edad}"

    @staticmethod
    def esMayorEdad(edad):
        return edad > 18

    @classmethod
    def crear_estudiante(cls, nombre, edad):
        if cls.esMayorEdad(edad):
            print(f"[+] Estudiante {nombre} con edad {edad}")
            return cls(nombre, edad)
        else:
            print(f"[-] No se agregaron {nombre} con edad {edad}")


cris = Estudiantes.crear_estudiante("cris", 30)
jose = Estudiantes.crear_estudiante("jose", 4)
