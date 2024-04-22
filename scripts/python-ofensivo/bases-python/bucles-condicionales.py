#!/usr/bin/env python3 

from rich import print 

separators="------------------------------------"
print(f"\n[green]{separators} Bucles For {separators}[/green]")
# For 
for i in range(5):
    print(i)

lista=["hola", "chao", "adios"]

for i in lista:
    print(i)

# while 

print(f"\n[green]{separators} Bucles while {separators}[/green]")

i=0
while i<5:
    i+=1
    print(i)


print(f"\n[green]{separators} Bucles enumerate {separators}[/green]")

names = ["Joss", "Cris","Carlito"]
for pos, name in enumerate(names):
    print(pos, name)


print(f"\n[green]{separators} lista de comprension {separators}[/green]")
lista = [1,2,3,4,5] 
lista_cuadrado=[i**2 for i in lista]
print("[blue]lista_cuadrado=[i**2 for i in lista][/blue]")
print(f"Lista: {lista}, Cuadrado: {lista_cuadrado}")


#? Break dermina con la iteracion de for y finalza el bucle
print(f"\n[green]{separators} break {separators}[/green]")
for i in range(10):
    if i == 5:
        print(f"i vale {i}/9 y break detiene bucle")
        break
    print(f"i vale {i}/9")
#? Continue pasa a la siguiente iteracion
print(f"\n[green]{separators} continue {separators}[/green]")
for i in range(10):
    if i == 5: 
        print(f"[+] i vale {i} salta condicion")
        continue
    print(i)

#? for else. al terminar el for ejecuta estas lineas de comando
print(f"\n[green]{separators} else {separators}[/green]")
for i in range(10):
    print(f"i vale {i}")
else:
    print("el for ha concluido")

#! Si hay un break el else no se ejecutara jamas



print(f"\n[green]{separators}  Condicionales  {separators}[/green]")

#Texto Condicionales
valor=2
texto = "Esto es un texto" if valor ==1 else "Este es el otro texto"

print(texto)



