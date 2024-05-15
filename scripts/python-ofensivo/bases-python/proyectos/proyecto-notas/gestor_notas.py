""" Clase gestionar notas """

import os
import pickle

from rich import print

from notas import Nota


class GestorNotas:
    """Class notas"""

    def __init__(self, archivo_notas="notas.pkl"):
        self.archivo_notas = archivo_notas

        try:
            with open(self.archivo_notas, "rb") as f:
                self.notas = pickle.load(f)
        except FileNotFoundError:
            self.notas = []

    def guardar_notas(self):
        """Guarda notas"""
        with open(self.archivo_notas, "wb") as f:
            pickle.dump(self.notas, f)

    def agregar_nota(self, contenido):
        """metodo agregar nota"""
        self.notas.append(Nota(contenido))
        self.guardar_notas()

    def mostrar_notas(self):
        """Metodo mostrar notas"""
        print(f"[green][+][/green] Mostrando todas las notas almacenadas \n")
        for index, content in enumerate(self.notas):
            print(f"{index} - {content} ")

    def buscar_nota(self, texto):
        """Metodo buscar en notas"""
        print("[green][+][/green] Buscando en notas...")
        for index, txt in enumerate(self.notas):
            if texto in txt.contenido:
                print(f"[green][+][/green] {index} - {txt}")

    def eliminar_nota(self):
        self.mostrar_notas()
        nota_a_eliminar = int(input("[?] Escoja la nota que desea eliminar: "))
        try:
            del self.notas[nota_a_eliminar]
            self.guardar_notas()
            os.system("cls" if os.name == "nt" else "clear")
            print(f"[green] Notas actualizadas...[/green]")
            self.mostrar_notas()

        except IndexError:
            print("[red][!] Indice erroneo[/red]")
