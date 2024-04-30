#!/usr/bin/env python3

"""Decoradores en pytnon"""


def my_decorador(funcion):
    def envoltura():
        print("envoltura")
        funcion()
        funcion().upper()
        print("envoltura")

    return envoltura


@my_decorador
def funcion_original():
    print("funcion")
    return "hola"


saludo = funcion_original()
