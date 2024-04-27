#!/usr/bin/env python
from rich import print


class Libro:

    # ? class variables
    best_seller_value = 5000
    IVA = 0.21

    def __init__(self, name, autor, price):
        self.name = name
        self.autor = autor
        self.price = price

    @staticmethod
    def isBestSeller(total_sales):
        #! Un método estático ya no hace uso del objeto y puede ser llamado por cualquiera
        return total_sales > Libro.best_seller_value

    @classmethod
    #! El método de clase nos ayuda a poder llamar variables propias de la clase para cada clase
    def precio_con_iva(cls, precio):
        return precio * (cls.IVA + 1)


# herencia de libro
class LibroDigital(Libro):
    IVA = 0.10


my_libro = Libro("Como ser un perfecto lammer", "kraken", 19.8)
my_libro_digital = LibroDigital("Como ser un hacker exitoso", "kraken", 19.8)

print(f"libro es bestseller: {Libro.isBestSeller(4999)}")
print(f"libro con iva: {Libro.precio_con_iva(my_libro.price)}")
print(f"libro digital: {LibroDigital.precio_con_iva(my_libro_digital.price)}")
