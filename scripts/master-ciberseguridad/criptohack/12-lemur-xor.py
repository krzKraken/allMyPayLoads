#!/usr/bin/env python3

from PIL import Image
import numpy as np

# Cargar las dos imágenes
img1 = Image.open("lemur.png").convert("RGB")
img2 = Image.open("flag.png").convert("RGB")

# Asegurar que ambas imágenes tienen el mismo tamaño
if img1.size != img2.size:
    raise ValueError("Las imágenes deben tener el mismo tamaño")

# Convertir imágenes en matrices NumPy
array1 = np.array(img1)
array2 = np.array(img2)

# Aplicar XOR en cada pixel (R, G, B)
decoded_array = array1 ^ array2

# Convertir de vuelta a imagen
decoded_image = Image.fromarray(decoded_array)

# Guardar o mostrar la imagen
decoded_image.show()  # Mostrar en pantalla
decoded_image.save("imagen_descifrada.png")  # Guardar

