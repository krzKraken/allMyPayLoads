#!/usr/bin/env python3

from rich import print 

#? class vehiculo
class Vehiculo:
  def __init__(self, marca, modelo):
    self.marca = marca
    self.modelo = modelo 
    
  def describir(self):
    return f""