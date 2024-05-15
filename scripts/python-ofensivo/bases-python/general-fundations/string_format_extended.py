#!/urs/bin/env python3

"""String formating"""


nombre = "Pepito"
edad = 29
estatura_cm = 167.5

# NOTE: Metodo 1

print(
    "hola, me llamo {}, tengo {} y mi estatura es {}".format(nombre, edad, estatura_cm)
)


# NOTE: Metodo 2
print(
    "hola, me llamo {0}, tengo {1} y mi estatura es {2}".format(
        nombre, edad, estatura_cm
    )
)

# NOTE: Metodo 3
print(f"hola, me llamo {nombre}, tengo {edad} y mi estatura es {estatura_cm}")
