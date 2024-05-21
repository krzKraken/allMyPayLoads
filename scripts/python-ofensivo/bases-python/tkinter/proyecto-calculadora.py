import tkinter as tk

class Calculadora:
    custom_font = ('Arial', 20)

    def __init__(self, master):
        self.master = master
        self.display = tk.Entry(self.master, font=self.custom_font, bd=10, insertwidth=1, bg='#6495DE', justify=tk.RIGHT)
        self.display.grid(row=0, column=0, columnspan=4)

        def clear_display(self):
            self.display.delete('1.0', tk.END)

        def set_number(num):
            print(f'numero..!!!{num}')

        def set_operacion(num):
            print('operacion', num)

        buttons_positions = {
            '7': (1, 0, '7', set_number),
            '8': (1, 1, '8', set_number),
            '9': (1, 2, '9', set_number),
            '/': (1, 3, '/', set_operacion),

            '4': (2, 0, '4', set_number),
            '5': (2, 1, '5', set_number),
            '6': (2, 2, '6', set_number),
            '*': (2, 3, '*', set_operacion),

            '1': (3, 0, '1', set_number),
            '2': (3, 1, '2', set_number),
            '3': (3, 2, '3', set_number),
            '-': (3, 3, '-', set_operacion),

            'C': (4, 0, 'C', set_number),
            '0': (4, 1, '0', set_number),
            '.': (4, 2, '.', set_number),
            '+': (4, 3, '+', set_operacion),
        }

        for button, pos in buttons_positions.items():
            b = tk.Button(master=self.master, text=button, width=5, command=lambda num=pos[2]: pos[3](num))
            b.grid(row=pos[0], column=pos[1])

# Ventana principal
root = tk.Tk()

# My objeto Calculadora pasando el root tkinter
my_gui = Calculadora(root)

root.mainloop()