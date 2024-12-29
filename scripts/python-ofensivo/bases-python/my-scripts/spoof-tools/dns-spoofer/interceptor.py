#!/usr/bin/env python3

import scapy.all as scapy


def process_packet(packet):
    if packet.haslayer(scapy.DNSRR):
        qname = packet[scapy.DNSQR].qname
        if b"google" in qname:
            print("\n--------------------\n")
            print(packet.show())


scapy.sniff(iface="ens33", filter="udp and port 53", prn=process_packet, store=0)
