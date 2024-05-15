#!/usr/bin/env python3

""" Hora y fecha date time  """

import datetime

# NOTE: Tiempo actual
print("datetime.datetime.now()) -> ", datetime.datetime.now())


# NOTE: Crear una fecha especifica
date = datetime.date(2023, 12, 30)
print("datetime.date(2023, 12, 30) -> ", date)


# NOTE: Crear una hora
hora = datetime.time(14, 40, 29)
print("datetime.time(14, 40, 29) -> ", hora)

# NOTE: Crear hora y fecha
fecha_hora = datetime.datetime(2023, 1, 30, 11, 40, 55)
print("datetime.datetime(2023, 1, 30, 11, 40, 55) -> ", fecha_hora)
print("fecha_hora.date() -> ", fecha_hora.date())
print("fecha_hora.time() -> ", fecha_hora.time())
print("datetime.datetime.now() -> ", datetime.datetime.now())
ahora = datetime.datetime.now()
print("fecha_hora.year ->", fecha_hora.year)
print("fecha_hora.minute ->", fecha_hora.minute)
print("fecha_hora.second ->", fecha_hora.second)


hora1 = datetime.time(20, 10, 55)
print(hora1)
hora2 = datetime.time(22, 22, 55)
print(hora2)
print(datetime.timedelta(hora1.second, hora2.second))
