#!/usr/bin/env python3

import tkinter as tk 

def get_data():
    print('\n[+] Datos introducidos por usuario: ')

root= tk.Tk()
root.geometry('500x500')

root.title('Entry() widget')

entry_widget= tk.Entry(root)
entry_widget.pack(pady=100)
button = tk.Button(root, text='Get data', command=get_data)
button.pack(side=tk.BOTTOM, padx=15, pady=20, fill=tk.X)

root.mainloop()


