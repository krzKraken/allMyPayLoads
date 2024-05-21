#!/usr/bin/env python3

import tkinter as tk
import sys

#NOTE: This function sends the data when the send_button is clicked 
def get_data():
    data = entry_widget.get()
    print(f"\n[+] Datos introducidos por usuario: {data}")
    #Clear the Entry data field before sending the data
    entry_widget.delete(0, tk.END)

#NOTE: This function sends the data from the text_widget whe send send_text_button is clicked 
def get_text_widget():
    data = text_widget.get("1.0", tk.END)
    print(f"\n[+] Datos introducidos por usuario: {data}")
    #Clear the text_widget data field before sending the data
    text_widget.delete("1.0", tk.END)


#NOTE: This function close the application
def exit_button():
    print("\n[+] Saliendo... \n")
    sys.exit(0)

#NOTE: Creates the page root 
root = tk.Tk()
root.geometry("500x500")

root.title("Entry() - Text() widget")

#Custom Font 
custom_font = ('hack nerd font', 20)

#Top label 
label_superior = tk.Label(text='Data Entry()', bg='gray', foreground='black', font=custom_font)
label_superior.pack(side=tk.TOP, fill=tk.X, padx=20, pady=10)

#Entry field (one line per line)
entry_widget = tk.Entry(root)
entry_widget.config( font=custom_font)
entry_widget.pack(padx=10, pady=20, fill=tk.X, anchor=tk.CENTER)


#Button send data Entry widget 
button_send_data = tk.Button(root, text="Get data Entry()", command=get_data)
button_send_data.pack(side=tk.TOP, padx=10, pady=20, fill=tk.X)

label_text = tk.Label(text='Text() widget entry', bg='gray', foreground='black', font=custom_font)
label_text.pack(side=tk.TOP, padx=10, pady=20, fill=tk.X, anchor=tk.CENTER)

#Text Field (many lines per line per)
text_widget = tk.Text(root, height=5)
text_widget.pack(pady=10, padx=20, side=tk.TOP, fill=tk.X, anchor=tk.CENTER)

#Text field get data
b_text_send_data = tk.Button(text='Text Entry()', command=get_text_widget)
b_text_send_data.pack(side=tk.TOP, padx=10, pady=20, fill=tk.X)

# Exit button 
button_exit = tk.Button(root, text="EXIT", command=exit_button)
button_exit.pack(side=tk.BOTTOM, padx=10, pady=10, fill=tk.X, anchor=tk.CENTER)
root.mainloop()













