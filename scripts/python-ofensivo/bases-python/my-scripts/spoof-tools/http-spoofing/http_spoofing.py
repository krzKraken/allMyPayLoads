#!/usr/bin/env python3

import re
import signal
import subprocess
import sys

import netfilterqueue
import scapy.all as scapy
from termcolor import colored


def def_handler(sig, frame):
    print(colored("\n[!] Saliendo...\n\n", "red"))
    sys.exit(1)


signal.signal(signal.SIGINT, def_handler)


def set_load(packet, load):
    packet[scapy.Raw].load = load
    print(packet.show())

    return packet


def process_packet(packet):
    scapy_packet = scapy.IP(packet.get_payload())
    if scapy_packet.haslayer(scapy.Raw):

        try:
            if scapy_packet[scapy.TCP].dport == 80:
                print("\n[+] Solicitud:\n")
                # NOTE: Modificando la capa raw.load para eliminar el parametro accetp-end
                modified_load = re.sub(
                    b"Accept-Encoding:.*?\\r\\n", b"", scapy_packet[scapy.Raw].load
                )
                # NOTE: construyendo la carga modificada
                new_packet = set_load(scapy_packet, modified_load)
                print(scapy_packet.show())

            elif scapy_packet[scapy.TCP].sport == 80:
                print("\n[+] Respuesta del servidor: \n")
                print(scapy_packet.show())
        except Exception as e:
            print(f"[!] Error: {e}")
    packet.accept()


def iptables_settings():
    subprocess.run(["iptables", "-I", "INPUT", "-j", "NFQUEUE", "--queue-num", "0"])
    subprocess.run(["iptables", "-I", "OUTPUT", "-j", "NFQUEUE", "--queue-num", "0"])
    subprocess.run(["iptables", "-I", "FORWARD", "-j", "NFQUEUE", "--queue-num", "0"])
    subprocess.run(["iptables", "--policy", "FORWARD", "ACCEPT"])


def main():
    iptables_settings()
    queue = netfilterqueue.NetfilterQueue()
    queue.bind(0, process_packet)
    queue.run()


if __name__ == "__main__":
    main()
