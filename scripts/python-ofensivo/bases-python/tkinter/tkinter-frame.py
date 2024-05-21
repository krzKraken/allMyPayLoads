#!/urs/bin/env python3 

import tkinter as tk 

# Ventana principal 
root = tk.Tk()
root.title('Frames demo')

# Frame dentro de la venatana principal 
frame = tk.Frame(bg='blue', bd=3)
frame.place(root, relx=0.5, rely=0.5, anchor=tk.CENTER)

# Labels 
label1 = tk.Label(text='Esto es un label1')
label1.pack(frame, side=tk.TOP, fill=tk.X)

label2 = tk.Label(text='Esto es el label2 ')
label2.pack(frame, side=tk.TOP, fill=tk.X)


root.mainloop()

