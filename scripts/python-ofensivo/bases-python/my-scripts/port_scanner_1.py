#!/usr/bin/env python3

import argparse
import socket
import sys

from termcolor import colored


def get_arguments():
    parser = argparse.ArgumentParser(description="Fast TCP Port Scanner")
    parser.add_argument(
        "-t",
        "--target",
        dest="target",
        help="Victim target to scan (Ex: -t 192.168.100.1)",
    )
    parser.add_argument(
        "-p",
        "--port",
        dest="port",
        help="Port range to scan (Ex: -p 1-100 or -p 80,443,8080)",
    )
    options = parser.parse_args()

    # NOTE: Imprime la ayuda si ejecuta incorrectamente el script
    if options.target is None or options.port is None:
        parser.print_help()
        sys.exit(1)
    return options.target, options.port


def create_socket():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1)
    return s


def port_scanner(port, host, s):
    try:
        s.connect((host, port))
        print(colored(f"\n[+] El puerto {port} esta abierto", "green"))
        s.close()

    except (socket.timeout, ConnectionRefusedError):
        s.close()


def scan_ports(ports, target):
    for port in ports:
        s = create_socket()
        port_scanner(port, target, s)


def parse_ports(port_str):
    if "-" in port_str:
        start, end = map(int, port_str.split("-"))
        return range(start, end + 1)
    elif "," in port_str:
        return map(int, port_str.split(","))
    else:
        return (int(port_str),)


def main():

    target, port_str = get_arguments()

    ports = parse_ports(port_str)

    scan_ports(ports, target)


if __name__ == "__main__":
    main()
