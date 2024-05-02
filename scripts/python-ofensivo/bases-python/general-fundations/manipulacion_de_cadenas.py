#!/usr/bin/env python3

# INFO: MANIPULACION DE CADENAS


# NOTE: Esto elimina los espacios en blanco
cadena = "Esto es una cadena hola mundo"
cadena = cadena.strip()
print("Cadena original:", cadena.strip())


# NOTE: lower , upper
print("lower: ", cadena.lower())
print("upper: ", cadena.upper())


# NOTE: Replace
print("cadena.replace('c','X'): ", cadena.replace("c", "X"))
print("cadena.replace(' ', ''): ", cadena.replace(" ", ""))

# NOTE: Split (el delimitador entre parentesis)
print("split(':'):", cadena.split(":"))

# NOTE: startswith()  endswith()
print("startswith('esto'): ", cadena.startswith("esto"))
print("endswith('mundo'): ", cadena.endswith("mundo"))


# NOTE: find() devuelve -1 si no encuentra
print("cadena.find(hola)", cadena.find("hola"))


# NOTE: index() devuelve ValueError si no encuentra
print('cadena.index("hola"): ', cadena.index("hola"))


# NOTE: count() contador de coincidencias de la lerta a
print("cadena.count('a'): ", cadena.count("a"))


# NOTE: join() unir iterables
print("'-'.join(cadena):", "-".join(cadena))

# NOTE: capitalize - title  -  swapcase
print("cadena.capitalize(): ", cadena.capitalize())
print("cadena.title()", cadena.title())
print("cadena.swapcase()", cadena.swapcase())

# NOTE: comprobaciones es alfabeto
cadena = "123asdf"
print("cadena.isalpha(): ", cadena.isalpha())
print("cadena.isdigit(): ", cadena.isdigit())
print("cadena.isalnumm():", cadena.isalnum())
print("cadena.isspace():", cadena.isspace())
print("cadena.isassci:", cadena.isascii())


# NOTE: Reemplazados avanzados
cadena = "hola soy cris y me gusta la playa"
print("cadena: ", cadena)
table = str.maketrans("aei", "AEI")
nueva_cadena = cadena.translate(table)
print(
    "table=str.maketrans('aei','AEI')\nnueva_cadena=cadena.trasnlate(table)\n nueva_cadena: ",
    nueva_cadena,
)
