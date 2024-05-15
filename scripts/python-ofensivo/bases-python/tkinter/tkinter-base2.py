#!/usr/bin/env python3

import tkinter as tk 

# Pagina root 

#NOTE: objeto tk.Tk()
root = tk.Tk()
root.title('hola')

label1 = tk.Label(root, text='mi primer label', bg='red', foreground='white')
label2 = tk.Label(root, text='mi segundo label', bg='blue', foreground='white')
label3 = tk.Label(root, text='mi tercer label', bg='orange', foreground='white')

label1.pack(fill=tk.X)
label2.pack(side=tk.BOTTOM, fill=tk.X)
label3.pack(side=tk.LEFT, fill=tk.Y)



root.mainloop()
