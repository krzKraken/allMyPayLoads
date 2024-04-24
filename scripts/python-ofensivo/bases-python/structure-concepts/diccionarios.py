#!/usr/bin/env python3

# Diccionario creacion
mi_diccionario = {"nombre": "krz", "edad": 33, "ciudad": "UIO"}
print(mi_diccionario)

# Agregar elementos a diccionario
mi_diccionario["sexo"] = "Masculino"
print(mi_diccionario)

# Lista elemento por llave
print(f"Imprimir elemento por nombre: {mi_diccionario['nombre']}")

# Reemplaza contenido
mi_diccionario["nombre"] = "nuevoNombre"
print(f"Diccionario actualizado: {mi_diccionario}")

# Verificar si existe en el diccionario (clave)
if "nombre" in mi_diccionario:
    print("Esta llave Existe")
else:
    print("Esta llave no existe")

# Barrer todo el diccionario con llave valor
for key, value in mi_diccionario.items():
    print(f"Key: {key}, Value: {value}")
