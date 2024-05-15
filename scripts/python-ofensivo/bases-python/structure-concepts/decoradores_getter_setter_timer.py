#!/usr/bin/env python3

import time

""" Ejemplo de decoradores """


# NOTE: los decoradores requieren la funcion de orden superior
def cronometro(funcion):
    def envoltura(num):
        inicia = time.time()
        funcion(num)
        finaliza = time.time()
        print(
            f"Tiempo total transcurrido en la funcion {funcion.__name__} es de : {finaliza - inicia}"
        )

    return envoltura


# NOTE: Decorador que envuelve la funcion y la manipula antes de la salida
@cronometro
def pausa_corta(num):
    time.sleep(num)


@cronometro
def pausa_larga(num):
    time.sleep(num)


pausa_corta(1)
pausa_larga(2)
