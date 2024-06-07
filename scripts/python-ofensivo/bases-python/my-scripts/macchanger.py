#!/usr/bin/env python3


import argparse
import re
import socket
import subprocess

from termcolor import colored


def get_arguments():

    parser = argparse.ArgumentParser(
        description="Herramienta para cambiar la direccion MAC de una interface de red"
    )
    parser.add_argument(
        "-i",
        "--interface",
        required=True,
        dest="interface",
        help="Nombre de la interface de red",
    )
    parser.add_argument(
        "-m",
        "--mac",
        required=True,
        dest="mac_address",
        help="Nueva direccion MAC para la interface de red",
    )

    return parser.parse_args()


def is_valid_input(interface, mac_address):
    available_interfaces = socket.if_nameindex()
    valid_interface = [i[1] for i in available_interfaces]
    if interface in valid_interface:
        print(colored(f"[+] La interface {interface} coincide", "green"))
        is_valid_mac_address = re.match(
            r"^([A-Fa-f0-9]{2}[:]){5}[A-Fa-f0-9]{2}$", mac_address
        )
        if is_valid_mac_address:
            print(colored(f"[+] La MAC address {mac_address} es valida", "green"))

            return True
        else:
            print(colored(f"[!] La MAC Address {mac_address} es invalida", "red"))
            return False

    else:
        print(
            colored(
                f"[+] La interface {interface} no coincide, interfaces disponibles {valid_interface}",
                "red",
            )
        )
        return False


def change_mac_address(interface, mac_address):
    # Validando la interface de macaddress
    if is_valid_input(interface, mac_address):
        subprocess.run(["ifconfig", interface, "down"])
        subprocess.run(["ifconfig", interface, "hw", "ether", mac_address])
        subprocess.run(["ifconfig", interface, "up"])
        print(f"\n[+] La MAC Address ha sido cambiada exitosamente")
        # Validando la nueva mac address
        subprocess.run(["ip", "addr", "show"])
        # print(colored(f"[+] La nueva mac_address es {result} ", "green"))

    else:
        print(colored(f"Los datos Introducidos no son correctos", "red"))


def main():

    args = get_arguments()

    change_mac_address(args.interface, args.mac_address)


if __name__ == "__main__":
    main()
