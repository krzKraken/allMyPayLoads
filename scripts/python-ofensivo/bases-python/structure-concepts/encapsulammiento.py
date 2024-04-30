#!/usr/bin/env python3
""" Encapsulamiento """


from rich import print


class Ejemplo:
    def __init__(self):
        """Atributo protegido"""
        self._atributo_protegido = "soy un atributo protegido y no deberias poder verme"

        """ Atributo privado """
        self.__atributo_privado = "soy un atributo privado y no deberias poder verme"

    def mostar_privados(self):
        print(self.__atributo_privado)


ejemplo = Ejemplo()
# atributo protegido es accesible
print(ejemplo._atributo_protegido)

# atributo privado no es accesibe de esta forma
# print(ejemplo.__atributo_privado)

#  Se accede de la siguiente manera a un atributo privado
ejemplo.mostar_privados()
