#!/usr/bin/env python3

from rich import print


class Libro:

    def __init__(self, id_libro, autor, nombre_libro):
        self.id_libro = id_libro
        self.autor = autor
        self.nombre_libro = nombre_libro
        self.esta_prestado = False

    def __str__(self):
        prestado = "- Esta prestado" if self.esta_prestado else "- En Stock"
        return f"[+] Libro ({self.id_libro}, {self.autor.title()},{self.nombre_libro.title()}) {prestado}"

    def __repr__(self) -> str:
        return self.__str__()


class Bibliotecla:
    def __init__(self):
        # libros no prestados # {1: Libro(1, "krzkraken", "Como ser un lammer"), 2: Libro(2, "pepito", "pepito y sus pepadas")
        self.libros = {}
        print(type(self.libros))

    def __str__(self):
        return f"{self.libros}"

    def agregar_libro(self, libro):
        if libro.id_libro not in self.libros:
            self.libros[libro.id_libro] = libro
            print(f"[+] Libro agregado correctamente: {libro}")

        else:
            print(
                f"\n[!] No es posible agregar el libro el ID: {libro.id_libro} ya existe"
            )

    def prestar_libro(self, id_libro):
        if id_libro in self.libros.keys():
            if self.libros[id_libro].esta_prestado == False:
                self.libros[id_libro].esta_prestado = True
            else:
                print("\n[!] El libro ya  se encuentra prestado")
        else:
            print("\n[!] El identifidor buscado no existe...")

    @property
    def mostrar_libros(self):
        """Retornar una lista que se obtiene"""
        libros_en_biblioteca = [
            libro for libro in self.libros.values() if not libro.esta_prestado
        ]
        print(f"[+] Libros en biblioteca: {libros_en_biblioteca}")
        return libros_en_biblioteca

    @property
    def libros_prestados(self):
        """Retorna listas de los libros prestados"""
        libros_prestados = [
            libro for libro in self.libros.values() if libro.esta_prestado
        ]
        print(f"[+] Libros prestados: {libros_prestados}")
        return libros_prestados


def main():
    biblioteca = Bibliotecla()

    libro1 = Libro(1, "kraken", "Mi libro, luna de pluton")
    libro2 = Libro(2, "s4vitar", "Como comer como bestia sin engordar")
    libro3 = Libro(3, "offsec", "La biblia del lammer")

    biblioteca.agregar_libro(libro1)
    biblioteca.agregar_libro(libro2)
    biblioteca.agregar_libro(libro3)

    print(f"\n[+] Libros en la biblioteca: {biblioteca.mostrar_libros}")
    biblioteca.prestar_libro(1)
    biblioteca.prestar_libro(2)

    print(f"\n[+] Libros en la biblioteca: {biblioteca.mostrar_libros}")
    biblioteca.libros_prestados


if __name__ == "__main__":
    main()
