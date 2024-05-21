import tkinter as tk 


root = tk.Tk()
root.configure(bg='gray')
root.geometry('500x500')

root.title('Canvas Tkinter')

label1 = tk.Label(text='Canvas', anchor=tk.CENTER, background='red')
label1.pack(side=tk.TOP, fill=tk.X)

canvas1 = tk.Canvas( height=300)
canvas1.pack(side=tk.TOP, fill=tk.X, padx=20, pady=20)

# Creando linea
canvas1.create_line(0,0,100,100, fill='green', width=3)

# Creando circulo
canvas1.create_oval(150,150,100,50, fill='red', width=2)

# Creando rectangle
canvas1.create_rectangle(0,0,100,100)
root.mainloop()

