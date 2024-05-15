#!/usr/bin/env python3

from rich import print 
separador ="---------------------------------------"

# Funciones sin retorno
print(f"[yellow]{separador} funcion sin retorno {separador}[/yellow]")
def my_funcion():
    print("Funcion sin retorno")

my_funcion()

# Funcion con argumento
print(f"[yellow]{separador} funcion con argumento {separador}[/yellow]")
def saludar(nombre):
    texto=f"hola, {nombre}"
    print(texto)
saludar("pepito")

# funcion con retorno
print(f"[yellow]{separador} funcion con retorno {separador}[/yellow]")
def suma(x,y):
    return x+y

respuesta = suma(10,20)
print(respuesta)


# funcion sin nombre lambda
print(f"[yellow]{separador} funcion sin nombre lambda {separador}[/yellow]")
my_funcion_lambda = lambda : "hola soy una funcion lambda"
print(my_funcion_lambda())


# funcion lambda con parametros
print(f"[yellow]{separador} funcion lambda con parametros {separador}[/yellow]")
cuadrado = lambda x:x**2
print(cuadrado(2))

# funcion lambda con multiple parametros
print(f"[yellow]{separador} funcion lambda multiple parametros {separador}[/yellow]")
suma_lambda = lambda x,y: x+y
print(suma_lambda(10,123))


# Funcion map 
# Funcion map recibe una funcion y un iterable, pero para devolver una lista tenemos que convertir a lista el map 
print(f"[yellow]{separador} funcion map {separador}[/yellow]")
numeros = [1,2,3,4,5,6]
cuadrados = list(map(lambda x: x**2, numeros))
print(cuadrados)

