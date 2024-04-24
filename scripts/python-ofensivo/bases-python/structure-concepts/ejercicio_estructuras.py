"""
Programa de lista de juegos

"""

from rich import print

#!/usr/bin/env python3

juego_categoria = {
    "Call of duty": "Guerra",
    "GTA5": "Aventura",
    "Batman": "Aventura",
}

juegos_y_stock = {
    "Call of duty": (400, 200),
    "GTA5": (223, 78),
    "Batman": (199, 97),
}

clientes = {
    "Call of duty": {"Cris", "Joss", "Carlos", "Juan"},
    "GTA5": {"Luis", "Cris", "Joss", "Pepe"},
    "Batman": {"Cris", "Juan"},
}


def resumen(juego):
    print(f"[+] El juego es de categoria:  {juego_categoria[juego]}")
    print(
        f"[+] Se ha vendido {juegos_y_stock[juego][0]} y tenemos de stock {juegos_y_stock[juego][1]}"
    )
    print(
        f"[+] los clientes que compraron el juego son: { ', '.join(clientes[juego])}\n"
    )


min = 300
for juego in juego_categoria.keys():
    if juegos_y_stock[juego][0] > min:
        print(f"[green] Resumen de ventas [/green]")
        resumen(juego)
ventas_totales = lambda: sum(
    ventas for ventas, stock in juegos_y_stock.values() if ventas > min
)

print(ventas_totales())
