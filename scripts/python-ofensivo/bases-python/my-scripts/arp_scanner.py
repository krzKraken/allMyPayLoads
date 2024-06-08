#!/usr/bin/env python3

import argparse
import signal
import sys

import scapy.all as scapy
from termcolor import colored

"""
ARP Scanner with scapy 
"""


def def_handler(sig, frame):
    print(colored("[+] Saliendo...\n\n", "red"))
    sys.exit(1)


signal.signal(signal.SIGINT, def_handler)


def get_arguments():
    parser = argparse.ArgumentParser(description="ARP Scanner using Scapy")
    parser.add_argument(
        "-t",
        "--target",
        dest="target",
        required=True,
        help="Set the target or range (Ex: 192.168.1.1 or 192.168.1.1-100 )",
    )
    options = parser.parse_args()
    return options.target


# Scapy for scan with ip basic
def scan_basic(ip):
    return scapy.arping(ip)


# Scapy for scan arp broadcast packet advance
def scan_arp_brodcast(ip):
    # ARP packet
    arp_packet = scapy.ARP(pdst=ip)
    # broadcast packet
    broadcast_packet = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    # Juntando los paquetes a enviar
    complete_packet = broadcast_packet / arp_packet  # -> Empaquetando para enviar
    # NOTE: Al enviar recibimos dos respuesta, los que responden y los que no
    answered_list = scapy.srp(complete_packet, timeout=1, verbose=False)[0]
    # NOTE: Scapy imprime en consola el resumen al llamar la funcion
    # print(colored(f"[+] Host activos:\n\t{response}", "green"))
    for sent, received in answered_list:
        print(f"Ip: {received.psrc} -> MAC: {received.hwsrc}")


def main():
    target = get_arguments()
    # scan_basic(target)
    scan_arp_brodcast(target)


if __name__ == "__main__":
    main()
