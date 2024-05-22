import tkinter as tk

class Calculadora:
    custom_font = ('Arial', 20)

    def __init__(self, master):
        self.master = master
        self.display = tk.Entry(self.master, font=self.custom_font, bd=10, insertwidth=1, bg='#6495DE', justify=tk.RIGHT)
        self.display.grid(row=0, column=0, columnspan=4)
        self.operacion=''
        self.valor_display = ''

        row = 1
        col = 0

        buttons= [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            'C', '0', '.', '+',	
            '='
        ]
        for button in buttons:
            self.build_button(button, row, col) 
            col += 1
            if col > 3:
                col = 0
                row += 1
        self.master.bind('<Key>', self.key_press)

    def key_press(self, event):
        key = event.char
        if key == '\r':
            self.calculate()
            return 
        elif key == '\b': 
            self.clear_display()
            return
        elif key == '\x1B':
            self.master.quit()
            return

        self.click(key)
        



    def calculate(self):
        if self.valor_display == '' or self.display.get()=='':
            self.display.delete(0, tk.END)
        else:
            valor=self.display.get()
            print(f'[+] Valor: {valor}')
            valor_anterior=self.valor_display
            print(f'[+] Valor_anterior: {valor_anterior}')
            operacion=self.operacion
            res = eval(str(valor_anterior) + str(operacion)  + str(valor))
            print(res)
            self.display.delete(0, tk.END)
            self.display.insert(0, str(res))
            self.valor_display=str(res)


    def build_button(self, button, row, col):
        if button=='C':
            b = tk.Button(self.master, text=button, width=10, command=self.clear_display)
        elif button == '=':
            b = tk.Button(self.master, text=button, width=10, command=self.calculate)
        else: 
            b = tk.Button(self.master, text=button, width=10, command=lambda: self.click(button))
        b.grid(row=row, column=col)
    
    def clear_display(self):
        self.display.delete(0, tk.END)

    def click(self,key):

        if any( operacion in '*+/-' for operacion in self.display.get() ):
            self.display.delete(0, tk.END)
            self.display.insert(tk.END, key)

        elif key in '1234567890.':
            print(self.display.get())
            self.display.insert(tk.END, key)
        elif key in '*+-/':
            self.operacion=key 
            self.valor_display=self.display.get()
            self.display.delete(0, tk.END)
            self.display.insert(0, key)

            

# Ventana principal
root = tk.Tk()

# My objeto Calculadora pasando el root tkinter
my_gui = Calculadora(root)

root.mainloop()
