#!/usr/bin/env python3

from rich import print 

separators = "---------------------------"

## String formating
print("\n[green]{0} String Formating {0}[/green]".format(separators))

print("\n[green]{0} Usando %s %d {0}[/green]".format(separators))
name="kraken"
edad=32
print("\nhola, me llamo %s y tengo %d años!" % (name, edad))

# .format posicionales
print("\n[green]{0} Usando .format posicionales{0}[/green]".format(separators))

print("hola, me llamo {} y tengo {} años!".format(name,edad))

# .format con index
print("\n[green]{0} Usando .format con indices{0}[/green]".format(separators))
print("hola, me llamo {0}, tengo {1} anos, no mentira me llamo {0}".format(name,edad))


print("\n[green]{0} Usando f\"\" con nombre[/green]".format(separators))
print(f"hola, me llamo {name} y tengo {edad} anos")
