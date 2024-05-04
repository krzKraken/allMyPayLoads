#!/usr/bin/env python3

""" Proyecto de notas y serializacion de datos con pickle  """
import os

from rich import print

from gestor_notas import GestorNotas


def main():

    gestor = GestorNotas()

    while True:
        print("[green]\n-------------\nMenu\n-------------\n[/green]")
        print("[blue]1[/blue]. Crear una nota")
        print("[blue]2[/blue]. Leer todas las notas")
        print("[blue]3[/blue]. Buscar por unas nota")
        print("[blue]4[/blue]. Eliminar una nota")
        print("[red]5. Salir[/red]")

        opcion = input("\n[+] Selecciona una opcion: ")

        if opcion == "1":
            contenido = input("\n[+] Contenido de la nota:")
            gestor.agregar_nota(contenido)
        elif opcion == "2":
            gestor.mostrar_notas()
        elif opcion == "3":
            texto_a_buscar = input("\n[?] Ingresa cual es contenido de busqueda? ")
            gestor.buscar_nota(texto_a_buscar)
        elif opcion == "4":

            print("[red]Menu de eliminacion[/red]")
            gestor.eliminar_nota()

        elif opcion == "5":
            break
        else:
            print("\n[red][!][/red]La opcion indicada es incorrecta\n")

        input(f"\n[+] Presiona <Enter> para continuar...")
        os.system("cls" if os.name == "nt" else "clear")


if __name__ == "__main__":
    main()
