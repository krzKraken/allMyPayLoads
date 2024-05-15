#!/usr/bin/env python

class Calculadora:

    @staticmethod
    def suma(num1, num2):

        return num1 + num2

    @staticmethod
    def resta(num1, num2):

        return num1 - num2

        print
    @staticmethod
    def multiplicacion(num1, num2):

        return num1 * num2
    
    @staticmethod    
    def division(num1, num2):

        return (
            num1 / num2 if num2 != 0 else "\n[-] No se puede dividir un numero entre 0"
        )

print( Calculadora.suma(1,2))
print( Calculadora.multiplicacion(2,2))