#!/usr/bin/env python3

import tkinter as tk

root = tk.Tk()

root.title("Frames bases")
root.geometry("500x400")

custom_font = ("Hack Nerd Fonts", 20)

label1 = tk.Label(
    root,
    text="Frames introction",
    font=custom_font,
    background="gray",
    foreground="black",
)


label1.pack(side=tk.TOP, fill=tk.X)

# NOTE: Frame 1 creado
frame1 = tk.Frame(root, bg="blue", bd=3)
frame1.place(relx=0.3, rely=0.3, anchor=tk.CENTER)

label2 = tk.Label(frame1, text="Texto dentro de frame", bg="white", background="red")
label2.pack()
label3 = tk.Label(frame1, text="Segundo texto", background="yellow")
label3.pack(side=tk.TOP, fill=tk.X)

# NOTE: Frame 2
frame2 = tk.Frame(root, bg="green", bd=10, width=500, height=200)
frame2.place(relx=0.7, rely=0.7, anchor=tk.CENTER)

label4 = tk.Label(
    frame2, text="Label en frame 2   sadfasdf asdfasfasdf", background="blue"
)
label4.pack(fill=tk.X)
label5 = tk.Label(frame2, text="Label en frame 2", background="red")
label5.pack(fill=tk.X)

root.mainloop()
