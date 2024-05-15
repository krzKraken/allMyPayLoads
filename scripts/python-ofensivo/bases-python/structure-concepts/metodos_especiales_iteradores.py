#!/usr/bin/env python3


class Contador:
    def __init__(self, limite):
        self.limite = limite

    def __iter__(self):
        self.contador = 0
        return self

    def __next__(self):
        if self.contador < self.limite:
            self.contador += 1
            return self.contador
        else:
            raise StopIteration


c = Contador(10)
for i in c:
    print(i)
