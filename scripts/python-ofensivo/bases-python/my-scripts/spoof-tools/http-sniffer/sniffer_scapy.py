#!/usr/bin/env python3


import signal
import sys

import scapy.all as scapy
from termcolor import colored


def def_handler(sig, frame):
    print(colored("[!] Saliendo...\n"))
    sys.exit(1)


signal.signal(signal.SIGINT, def_handler)


def process_dns_packet(packet):
    if packet.haslayer(scapy.DNSQR):
        domain = packet[scapy.DNSQR].qname.decode()

        exclude_keywords = ["google", "cloud", "bing", "static"]

        if domain not in domains_seen and not any(
            keyword in domain for keyword in exclude_keywords
        ):
            domains_seen.add(domain)
            print(f"[+] Dominio: {domain}")

    # print(packet)


def sniff(interface):
    global domains_seen
    domains_seen = set()
    # NOTE: Scapy tiene el metodo sniff y aplica filtros como tambien un llamado a una funcion 'prn' para
    # procesar los paquetes y store para no almacenarlos
    scapy.sniff(
        iface=interface, filter="udp and port 53", prn=process_dns_packet, store=0
    )


def main():
    sniff("ens33")


if __name__ == "__main__":
    main()
