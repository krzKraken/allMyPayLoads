#!/usr/bin/env python3

class Automovil:
  def __init__(self, marca, modelo):
    self.marca = marca
    self.modelo = modelo
  
  def __str__(self):
    return f"Class automvil: marca -> {self.marca} y modelo -> {self.modelo}"
  
  
  """decorador methodclass """
  @classmethod
  def deportivo(cls, marca):
    return cls(marca, "Deportivo")
  
  @classmethod
  def muscle(cls, marca):
    return cls(marca, "muscleCar")

my_lambo = Automovil("Lamborginni", "Murcielago")
print(my_lambo)

my_pichirilo = Automovil.deportivo("VV")
print(my_pichirilo)

my_camaro = Automovil.muscle("Camaro Z28")
print(my_camaro)
