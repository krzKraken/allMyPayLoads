#!/usr/bin/env python3

""" Demostracion de aplicacion de hilos """

import threading
import time


def tarea(num_tarea):
    print(f"\n[+] iniciando tarea {num_tarea}")
    time.sleep(2)
    print(f"\n[+] Terminando tarea {num_tarea}")


# NOTE: Define los hilos
thread1 = threading.Thread(target=tarea, args=(1,))
thread2 = threading.Thread(target=tarea, args=(2,))

# NOTE: Arranca los hilos
thread1.start()
thread2.start()

# NOTE: Espera que los hilos terminen antes de continuar con el programa
# thread1.join()
# thread2.join()

# NOTE: Continua el program a
print(f"\n[+] Los hilos han finalizado exitosamente")
