#!/usr/bin/env python3

import tkinter as tk
from tkinter import messagebox, filedialog
import sys

class SimpleTextEditor:
  def __init__(self, root):
    self.root= root
    self.text_area=tk.Text(self.root)
    self.text_area.pack(fill=tk.BOTH, expand=1)
    self.current_file= ''
  
  # Funcion Nuevo
  def new_file(self):
    self.text_area.delete('1.0', tk.END)
    
  # Funcion Guardar
  def save_file(self):
    if not self.current_file:
      new_file_path=filedialog.asksaveasfilename()
      if new_file_path:
        self.current_file=new_file_path
      else:
        return
      with open(self.current_file, 'w') as file:
        file.write(self.text_area.get('1.0', tk.END))
  
  # Funcion Salir
  def quit_confirm(self):
      resp = messagebox.askokcancel(title='Salir?', message='Estas seguro que quieres salir?')
      if resp == True:
        #INFO: Si es True o acepta destruye la ventana root (SALE)
        root.destroy()


  # Abrir un archivo y llenar el text
  def open_file(self):
    filename = filedialog.askopenfilename()
    if filename:
      self.text_area.delete('1.0', tk.END)
      with open(filename, 'r') as file:
        self.text_area.insert('1.0',file.read())
      self.current_file=filename
#NOTE: Crea ventana root
root = tk.Tk()
root.title("Proyecto Menu") # titulo
root.geometry('700x500')

editor = SimpleTextEditor(root)

menu_bar = tk.Menu(root) # Crea barra en root



      
# Crea opciones en menu
menu_opcions = tk.Menu(menu_bar, tearoff=0)
menu_opcions.add_cascade(label="Nuevo", command=editor.new_file)
menu_opcions.add_cascade(label="Abrir", command=editor.open_file)
menu_opcions.add_cascade(label="Guardar", command=editor.save_file)
menu_opcions.add_cascade(label="Salir", command=editor.quit_confirm)

# NOTE: Pinta la barra menu bar en root
root.config(menu=menu_bar)
#INFO: En la menu barra agrega las opciones dentro del menu
menu_bar.add_cascade(label="Archivo", menu=menu_opcions)


root.mainloop()
