#!/usr/bin/env python3

""" *args y *kwargs """

# NOTE: las funciones pueden recibir parametros posicionales, o con nombre


def saludar(nombre):
    """Funcion saludar con un argumento"""
    print(f"hola {nombre}")


saludar("Cris")


def llamar_personas(*args):
    """Funcion con argumentos recibidos en tuplas"""
    print(f"llamando a: {', '.join(args)}")


llamar_personas("Cris", "Joss", "Carlito")


def detalle_persona(**kwargs):
    """Funcion recibe parametros con nombre en diccionario"""
    print(f"Detalle de persona: {kwargs}")
    print(kwargs["nombre"])


detalle_persona(nombre="Cris", edad=32, profesion="lammer")


def animales_dueno(*args, **kwargs):

    print(f"mascotas: {', '.join(args)} \nInfo del dueno: {kwargs['nombre']}")


animales_dueno("pocho", "michi", nombre="Kraken", edad=21)
