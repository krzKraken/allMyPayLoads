import tkinter as tk 
from tkinter import messagebox, filedialog


root = tk.Tk()
root.title('Widget menu')

#Funcion cuando se presiona el menu
def accion_menu():
  # Ventana informativa 
  messagebox.showinfo('Titulo', 'mensaje se tensa')

# accion boton
def accion():
  messagebox.showinfo(title='boton informa', message='Me has presionado')

# Abrir archivo
def abrir_archivo():
  ruta_archivo=filedialog.askopenfilename()
  print(f'[+] Ruta del archivo: {ruta_archivo}')

# Menus (barra de menu y las opciones)
# Crea la barra de menu
barra_menu= tk.Menu(root)
# Incorpora la barra de meny al root
root.config(menu=barra_menu)

# elimina la desfragmentacion
menu1 = tk.Menu(barra_menu, tearoff=0)

barra_menu.add_cascade(label='Menú', menu=menu1)

menu1.add_command(label='opcion 1')
menu1.add_command(label='opcion 2')


menu2 = tk.Menu(barra_menu, tearoff=0)
barra_menu.add_cascade(label='Extras', menu=menu2)

menu2.add_command(label='se tensa', command=accion_menu)

botton = tk.Button(root, text='Presioname', command=accion)
botton.pack(side=tk.BOTTOM)

boton_file=tk.Button(root, text='find file', command=abrir_archivo)
boton_file.pack(side=tk.BOTTOM)



root.mainloop()