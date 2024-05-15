#!/usr/bin/env python

import re

# INFO: Expresiones regulares
# \d -> digitos
# \w -> alfanumerico
# \w+ -> letras, las que sean
# \d{2,}  -> minimo 2 digitos hasta los que sean
# \d{2,4} -> Minimo 2 digitos hasta 4 digitos
# [A-Za-z0-9.!-_] -> busca entre estas coincidencias
# \bcar -> Todo lo que empieza con "car"
# car\b -> todo lo que termina con "car"

"""
.	    any characterls except newline
\w\d\s	word, digit, whitespace
\W\D\S	not word, digit, whitespace
[abc]	any of a, b, or c
[^abc]	not a, b, or c
[a-g]	character between a & g
Anchors
^abc$	start / end of the string
\b\B	word, not-word boundary
Escaped characters
\.\*\\	escaped special characters
\t\n\r	tab, linefeed, carriage return
Groups & Lookaround
(abc)	capture group
\1	backreference to group #1
(?:abc)	non-capturing group
(?=abc)	positive lookahead 
(?!abc)	negative lookahead
Quantifiers & Alternation
a*a+a?	0 or more, 1 or more, 0 or 1
a{5}a{2,}	exactly five, two or more
a{1,3}	between one & three
a+?a{2,}?	match as few as possible
ab|cd	match ab or cd
"""

# NOTE: Buscando coincidencias en un texto
text = "hola esto es un texto que tiene muy poco texto"
coincidencia = re.findall("texto", text)
print(coincidencia)

# NOTE: Buscando coincidencias en una fecha
text = "hoy es 10/12/2023 y manana sera 11/12/2023"
coincidencia = re.findall(r"\d{2}\/\d{2}\/\d{4}", text)
print(coincidencia)

# NOTE: patrones de busquedas con grupos kraken@gmail.com -> (kraken, gmail.com)
text = (
    "los usuarios pueden contactarnos a ina1!fo_hjola@gmail.com kraken123@hotmail.com"
)
coincidencia = re.findall(r"(\w+)@(\w+\.\w{2,})", text)
print(coincidencia)

# NOTE: Substituciones con el metodo subs
text = r"mi gato esta en el tejado y mi perro esta en el jardin"
coincidencia = re.sub("gato", "perro", text)
print(coincidencia)

# NOTE: re.split para separar en listas por alguna coincidencia
text = "campo1, campo2, campo3, campo4, campo5"
coincidencia = re.split(",", text)
print(coincidencia)


# NOTE: Validador de correo
correo = "kraken_1insane@yahoo.com"
patron = r"\b[A-Za-z0-9._-]+@[A-Za-z0-9._-]+\.[A-Za-z]{2,}\b"
coincidencia = re.findall(patron, correo)
print(coincidencia)


# NOTE: Capturador de fecha normal
text = "Hoy estaos 10/10/2020 y manana estaremos 11/10/2020"
patron = r"\b(\d{2}\/\d{2}\/\d{4})"
coincidencia = re.findall(patron, text)
print(coincidencia)

# NOTE: Capturador de fecha en bucle re.finditeer()
text = "Hoy estaos 10/10/2020 y manana estaremos 11/10/2020"
patron = r"\b(\d{2}\/\d{2}\/\d{4})"
for match in re.finditer(patron, text):
    print(
        f"Se ha encontrado coincidencias para {match.group(0)} desde {match.start()} hastas {match.end()}"
    )

# NOTE: Buscador de direcciones web hhtps y http
text = "la direccion url es https://holacomoestas.com.ec  y el inseguro es http://hola_ete.esotro.com.ec"
patron = r"\b(https\:\/\/\w+\.\w+\.\w+\b)|\b(http)\:\/\/\w+\.\w+\.\w+\b"
coincidencia = re.findall(patron, text)
print(coincidencia)
