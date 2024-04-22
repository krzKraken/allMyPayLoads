#!/usr/bin/env python3
from functools import partialmethod
from rich import print

sep = "-------------------------------------------"

print(f"[green]{sep} Conceptos de lista {sep}[/green]")

puertos_tcp=[21,22,25,5,443,445,229]


# longitud de lista 
print(f"[green]{sep} len lista  {sep}[/green]")
print(f"longitud de lista: {len(puertos_tcp)}")

# Agregar 1 elemento  a la lista
print(f"[green]{sep} append {sep}[/green]")
puertos_tcp.append(1003)
print(f"Puertos actuales: {puertos_tcp}")
print(f"Puerto 1003 agregado a lista: {puertos_tcp}")
 
# Agregar mas se un elemento a la lista 
print(f"[green]{sep} extend {sep}[/green]")

print(f"lista 1: {puertos_tcp}")
puertos_extras = [1,2,3,4]
puertos_tcp.extend(puertos_extras)
print(f"lista 2: {puertos_extras}")

print(f"lista de puertos puertos_tcp.extend(puertos_extras): {puertos_tcp}")

# Eliminar elemento por nombre de elemento k
print(f"[green]{sep} list.remove(name) {sep}[/green]")
cve_list=['CVE-2023-1234', 'CVE-2023-2212','CVE-2024-2342']
print(f"lista CVE:  {cve_list}")
cve_list.remove('CVE-2023-2212')
print(f"cve_list.remove('CVE-2023-2212') => {cve_list}")

# Ordenamiento de lista
print(f"[green]{sep} list.sort() {sep}[/green]")
print(f"Lista puertos tcp desordenados: {puertos_tcp}")
# Ordena los elementos en la lista, devuelve none 
puertos_tcp.sort()
# print(puertos_sort)
print(f"Lista puertos_tcp.sort(): {puertos_tcp}")


# invertir los elementos de una lista 
print(f"[green]{sep} letras.reverse() {sep}[/green]")
letras = ['a','b','c','d','e']
print(f"Lista letras original: {letras}")
letras.reverse()
print(f"Lista letras.reverse(): {letras}")

# Acceder a los elementos de una lista 
print(f"[green]{sep}  {sep}[/green]")
print("elemento pos 0 de letras {letras[0])}")
