#!/usr/bin/env python3

# WARN: Require <sudo apt instal python3-tk>

import sys
import tkinter as tk


def action_boton():
    print(f"\n[+] Se presionado el boton...")
    sys.exit(0)


# NOTE: Ventana principal
root = tk.Tk()

# Nombre ventana
root.title("Mi primera aplicacion")

# Label (mostar informacion)
label = tk.Label(text="hola mundo!")

# representar un label -> pack(), grip(), place()
label.pack()

# boton
boton = tk.Button(root, text="Presioname..", command=action_boton)
boton.pack()

# Ejecutar nuestra ventana de forma recursiva
root.mainloop()
