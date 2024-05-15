#!/usr/bin/env python3

import multiprocessing
import time


def tarea(num_tarea):
    print(f"\n[+] Tarea {num_tarea} iniciando")
    time.sleep(2)
    print(f"\n[+] Tarea {num_tarea} finalizando")


# NOTE: Inicializando los multiprocesos
proceso1 = multiprocessing.Process(target=tarea, args=(1,))
proceso2 = multiprocessing.Process(target=tarea, args=(2,))

# NOTE:Arrancando lo procesos
proceso1.start()
proceso2.start()

# NOTE: Esperando que terminen para continuar en el codigo
proceso1.join()
proceso2.join()

print(f"\n[+] Los procesos han finalizados exitosamente")
