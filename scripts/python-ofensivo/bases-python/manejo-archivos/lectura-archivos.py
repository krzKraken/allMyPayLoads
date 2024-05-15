""" Lectura de archivos """

# f = open("etc.host.txt", "r")
# print(f.read())
# f.close()
#

# NOTE: Si el archivo contienen caracteres especiales o es unbinario o fotografia se coloca el rb o wb o b para decirle que es otro tipo de dato
""" Leer archivos muy grandes """
with open("host.txt", "rb") as f_in:
    for i in f_in:
        print(i.strip().decode())

# NOTE: Para escribir en archivos tenemos que colocar el metodo de escritura en w .

with open("test.txt", "w") as f:
    f.write("hola mundo")

print("----- leyendo el archivo -------")
with open("test.txt", "r") as file:
    print(file.read())


# HACK: Una forma elegante de leer un archivo seria...
print("leyendo desde metodo elegante cariño")

file_name = "test.txt"
try:
    with open(file_name, "r") as f:
        print(f.read())
except FileNotFoundError:
    print(f"\n[!] No se ha encontrado el archivo {file_name} en el directorio")
