""" Funciones de calculadora """


def suma(x, y):
    return x + y


def resta(x, y):
    return x - y


def multiplicacion(x, y):
    return x * y


def division(x, y):
    if y != 0:
        return x / y
    else:
        raise ValueError("[-] No se puede dividir para 0")
