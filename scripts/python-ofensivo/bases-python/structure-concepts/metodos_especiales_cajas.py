#!/usr/bin/env python3

""" Metodos especiales """

from rich import print


class Cajas:
    def __init__(self, *items):

        self.items = items
        print(
            f"[green][+][/green] La caja se lleno de:[yellow] {', '.join(self.items)}[/yellow]"
        )

    # NOTE: Pyhton no sabe que es el metodo len de esta clase por lo que podemos especificarla

    def __len__(self):
        """Metodo especial len"""
        return len(self.items)

    def __getitem__(self, index):
        """Metodo especial getitem"""
        return self.items[index]


caja = Cajas("manzana", "pera", "banana")
print("[+] el metodo especial creado len: ", len(caja))
print(f"[+] Los elementos en la caja son: {', '.join(caja.items)}")
print(f"[+] El elemento en la posicion 1: es {caja[1]}")
