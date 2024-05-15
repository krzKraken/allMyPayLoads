#!/home/krzkraken/.venv/bin/python3
"""shban"""

from rich import print

SEP = "----------------------------"

print(f"{SEP} tuplas {SEP}")

mi_tupla = (1, 2, 3, 4, 5)

print("las tuplas no permiten los metodos: pop, remove, extend, insert, append  ")


# Se pueden usar para declarar variables
tupla_variables = ("Krz", "lammer", 33, "python")
name, profession, age, skills = tupla_variables
print(f"Mi nombre es {name}, tengo {age}, soy un {profession} y se {skills}")


# Se pueden sumar tuplas
tupla1 = (1, 2, 3, 4, 5)
tupla2 = (4, 5, 6, 7, 9)

tupla_suma = tupla1 + tupla2
print(tupla_suma)
