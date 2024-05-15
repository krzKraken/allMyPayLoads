#!/usr/bin/env python3

import tkinter as tk 
import sys 

def button_salir():
    print('\n[+] Saliendo...\n')
    sys.exit(0)
root = tk.Tk()

root.title('Grid settings')

b_salir=tk.Button(text='Exit',bg='red', foreground='white', command=button_salir)

label1 = tk.Label(text='Label1', bg='red', foreground='white')
label2=tk.Label(text='label2', bg='green', foreground='white')
label3 = tk.Label(text='label3', bg ='blue', foreground='white')
label1.grid(row=0, column=0)
label2.grid(row=0, column = 1)
label3.grid(row=1, column=1 ,columnspan=2 )
# b_salir.grid(row=3, column=7, columnspan=2)

root.mainloop()
