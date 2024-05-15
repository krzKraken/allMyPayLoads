#!/usr/bin/env python3


class Pizza:
    def __init__(self, size, *ingredientes):
        self.size = size
        self.ingredientes = ingredientes

    def detalle_pedido(self):

        return f"\n[+] Se ordeno una pizza de {self.size} pedazos, con los siguientes ingredientes: {', '.join(self.ingredientes)}"


pizza = Pizza(12, "tomate", "champinones", "cebolla", "carne")
print(pizza.detalle_pedido())
