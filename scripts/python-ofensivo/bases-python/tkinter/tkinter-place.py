#!/usr/bin/env python3

import tkinter as tk 
import sys 

root = tk.Tk()
root.geometry('800x100')
root.title('Place')

def button_exit():
    print('\n[+] Saliendo...')
    sys.exit(0)

label1 = tk.Label(text='Este es el label 1', bg='red', foreground='white')
label2 = tk.Label(text='Este es el label 2', bg='blue', foreground='white')
label3 = tk.Label(text='Este es el label 3', bg='green', foreground='white')
b_exit= tk.Button(text='Salir', bg='gray', foreground='black',command=button_exit)


label1.place(x=20, y=20)
label2.place(relx=.8, rely=.2)
label3.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
b_exit.pack(side='bottom')  
root.mainloop()
