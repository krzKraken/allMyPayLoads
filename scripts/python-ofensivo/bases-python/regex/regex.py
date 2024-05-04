#!/usr/bin/env python

import re 

#INFO: Expresiones regulares 
# \d -> digitos 
# \w -> alfanumerico 
# \w+ -> letras, las que sean 
# \d{2,}  -> minimo 2 digitos hasta los que sean
# \d{2,4} -> Minimo 2 digitos hasta 4 digitos 


#NOTE: Buscando coincidencias en un texto
text = "hola esto es un texto que tiene muy poco texto"
coincidencia = re.findall( "texto", text )
print(coincidencia)

#NOTE: Buscando coincidencias en una fecha
text = "hoy es 10/12/2023 y manana sera 11/12/2023"
coincidencia = re.findall('\d{2}\/\d{2}\/\d{4}', text)
print(coincidencia)

