#!/usr/bin/env python3


import scapy.all as scapy


def process_dns_packet(packet):
    print(packet)


def main():
    interface = "ens33"
    # NOTE: Scapy tiene el metodo sniff y aplica filtros como tambien un llamado a una funcion 'prn' para
    # procesar los paquetes y store para no almacenarlos
    scapy.sniff(
        iface=interface, filter="udp and port 53", prn=process_dns_packet, store=0
    )


if __name__ == "__main__":
    main()
