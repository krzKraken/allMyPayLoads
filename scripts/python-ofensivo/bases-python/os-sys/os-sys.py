#!/usr/bin/env python3

""" Libreria sys """
import os
import sys

from rich import print

# NOTE: Validando que un archivo existe

os.system("for i in $(seq 1 5); do touch file$i.txt; done ")


if os.path.exists("mi_archivo.txt"):
    print("[green][+][/green] os.path.exists('file') ->  Archivo Existe")
else:
    print("[red][!][/red] El archivo no existe... creando...")
    with open("mi_archivo.txt", "w") as file:
        file.write("hola csm")

# NOTE: Validando si existe un directorio, sino creandolo
if not os.path.exists("mi_directorio"):
    print(
        "[red][!][/red] if not os.path.exists('directorio') -> directorio no existe, creandolo...."
    )
    print('[green][+][/green] os.mkdir("directorio")  Creando direcorios ...')
    os.system("ls")

# NOTE: Validando directorio sino creandolo con su ruta anidada

if not os.path.exists("mi_directorio/mi_subdirectorio"):
    print(
        '[green][+][/green] os.makedirs("directorio/sub_directorio") -> Creando directorio'
    )
    os.makedirs("mi_directorio/mi_subdirectorio")


# NOTE: Listando todos los recursos en el directorio
print("[green][+][/green] listando recursos en el directorio actual\n")
print('for i in os.listdir(): print("recursos")\n')
recursos = os.listdir()
for recurso in recursos:
    print(recurso)

# NOTE: Eliminar archivos
print('\n[green][+][/green] os.remove("archivo") -> Eliminando archivo ')
if os.path.exists("mi_archivo.txt"):
    os.remove("mi_archivo.txt")
    os.system("ls")

# NOTE: Eliminando directorios
print(
    "\n[green][+][/green] os.rmdir('directori-vacio') -> Eliminando directorio vacio (si tiene algo dentro no funciona)"
)

os.mkdir("directorio_prueba")
if os.path.exists("directorio_prueba"):
    os.rmdir("directorio_prueba")
    print("[green][+][/green] Directorio eliminado")


# HACK: Utilizando shutil -> Eliminar directorio y subdirectorios
import shutil

# NOTE: shutil puede eliminar directorios y subdirectorios
if os.path.exists("mi_directorio"):
    print("[green][+][/green] Directorio actual: ")
    print(os.listdir())
    print(
        "[green][+][/green] shutil.rmtree('directorio') -> Eliminando el directorio y subdirectorios"
    )
    shutil.rmtree("mi_directorio")
    print("[green][+][/green] Listando recuros pos eliminacion: ")
    print(os.listdir())

# NOTE: shutil puede copiar archivos
if os.path.exists("file1.txt"):
    if os.path.exists("otro_directorio"):
        print(
            "[green][+][/green] shutil.copy('archivo', 'ruta') Moviendo directorio a directorio-2"
        )
        shutil.copy("file1.txt", "otro_directorio")
    else:
        print('\n[-] Directorio "otro-directorio" no existe... creandolo...')
        os.mkdir("otro_directorio")
        shutil.copy("file1.txt", "otro_directorio")


# NOTE: shutil puede copiar directorios y subdirectorios
if os.path.exists("directorio"):
    print('[green][+][/green] shutil.copytree("directorio", "otro_directorio")')
    # shutil.copytree("directorio", "otro_directorio")


# NOTE: Renombrando recursos con os.rename('origen.txt', 'nuevo_nombre.txt')
if os.path.exists("file1.txt"):
    print(
        "\n [green][+][/green] os.rename('file.txt', 'nuevo_nombre.txt') -> renombrando file1.txt a nuevo_file.txt"
    )
    print(os.listdir())
    os.rename("file1.txt", "nuevo_file.txt")
    print(os.listdir())
    os.rename("nuevo_file.txt", "file1.txt")


# NOTE: Determinando el peso de un archivo
if os.path.exists("/etc/passwd"):
    tamano = os.path.getsize("/etc/passwd")
    print(
        '\n[green][+][/green] os.path.getsize("/etc/passwd") -> Determinando el peso del archivo /etc/passwd'
    )
    print(f"El archivo /etc/passwd pesa {tamano} bytes")


# NOTE: Basename and dirname
path = os.path.join("directorio", "archivo.txt")
print(
    f'[green][+][/green] os.path.join("directorio","archivo.txt") -> creando path {path}'
)
print(f"os.path.basename(path) -> {os.path.basename(path)} ")
print(f"os.path.dirname(path) -> {os.path.dirname(path)}")
print(f"os.path.split(path) -> {os.path.split(path)}")


# NOTE: os.getcwd() -> pwd
current_directory = os.getcwd()
print(f"os.getcwd() -> {current_directory}")


# NOTE: os.listdir(path)
files_in_current_dir = os.listdir(current_directory)
print(f"os.listdir(path) -> ")
for file in files_in_current_dir:
    print(f"[+] File: {file}")

# NOTE: os.getenv() Obtener variables de entorno
get_env = os.getenv("KITTY_INSTALLATION_DIR")
print(f"os.getenv(KITTY_INSTALLATION_DIR) -> {get_env}")


# NOTE: Nombre del script
nombre_script = sys.argv[0]

print(f"[+] El nombre del script: {sys.argv[0]}")

# NOTE: Numero de argumentos pasados al script
len_args = len(sys.argv)
print(f"[+] El numero de argumentos pasados es: {len_args}")

# NOTE: Mostrando todos los argumentos
print(f"\n------[ Mostrando todos los argumentos pasados ]------")
for index, arg in enumerate(sys.argv):
    print(f"[+] Argumento {index} - {arg}")

# NOTE: Listando los argumentos enviados
print(f"\n----(Mostrando los argumentos enviados)------")
print(f"Los argumentos recibidos son: {', '.join(sys.argv[1:])}")

# NOTE: Mostrando las path de python
path_python = sys.path
print("\n------[Mostrando las rutas de pathon--------]")
for i in path_python:
    print("[+]", i)

# NOTE: Salir de forma forzada del progarma exit(1)
# print("[+] Saliendo del program con codigo de estado 1 (no exitoso)")
# sys.exit(1)

# NOTE: Salir de forma forzada del programa exitosamente
print('[+] Saliendo del programa con codigo de estado exitoso "exit(0)"')
sys.exit(0)
