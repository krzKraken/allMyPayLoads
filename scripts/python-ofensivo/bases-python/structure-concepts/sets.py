#!/usr/bin/env python3

print("---------------------- Conjuntos ----------------------")

# Sirven para eliminar repetidos en listas
lista_numeros = [1, 2, 3, 2, 23, 3, 1, 23, 4, 2, 32]
print(f"lista numeros {lista_numeros}")
print(f"lista numeros sin repetiviones  {list(set(lista_numeros))}")

# conjuntos no tiene elementos repetidos
set_names = {"kris", "Joss", "Paul", "Stefania"}
print(f"set de nombres: {set_names}")

# Agregando elementos a un conjunto
set_names.add("nuevo_elemento")
print(f"Agregando elemento con .add: {set_names}")

# Metodos de conjuntos o sets
set_names2 = ["kris", "Carlos", "Luis"]
print(f"lista de nombres 2: {set_names2}")

# Metodo interception
set_intercept = set_names.intersection(set_names2)
print(f"Metodo interception setnames1 setnames2: {set_intercept}")

# Metodos union
set_union = set_names.union(set_names2)
print(f"Metodo union setnames2: {set_union}")

# Metodo issuset
print(f"Metodo issuset: {set_names.issubset(set_names2)}")

# Metodo difference
set_difference = set_names.difference(set_names2)
print(f"Metodo difference {set_difference}")
