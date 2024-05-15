#!/usr/bin/env python3 

from rich import print 

#! Herencia
class Animal:
  def __init__(self, nombre):
    self.nombre = nombre
  
  def hablar(self, ):
    raise NotImplementedError
  
class Gato(Animal):
  
  def hablar(self):
    return f"Soy {self.nombre} y hago Miau!"
  
class Perro(Animal):
  
  def hablar(self):
    return f"soy {self.nombre} y hago Guau!"
  
'''La clase Gato hereda de la Clase Animal y hereda sus propiedades y metodos'''
gato = Gato("Federico")
perro = Perro("Tomas")

print("[green] {0} Herencia {0} [/green]".format( "*"*30))
print(gato.hablar())
print(perro.hablar()) 

#! Polimorfismo
def hacer_hablar(objeto):
    nombre = objeto.nombre
    print(f"Soy {nombre} y hago {objeto.hablar()}")

print("[green] {0} Polimorfirmo {0} [/green]".format( "*"*30))
hacer_hablar(gato)
hacer_hablar(perro)


