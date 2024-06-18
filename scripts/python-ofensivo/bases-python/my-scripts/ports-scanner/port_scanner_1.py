#!/usr/bin/env python3

import argparse
import signal
import socket
import sys
import threading

from termcolor import colored

open_sockets = []


def def_handler(sig, frame):
    print(colored("[+] Saliendo...\n\n", "red"))
    for socket in open_sockets:
        socket.close()
    sys.exit(1)


signal.signal(signal.SIGINT, def_handler)


def get_arguments():
    parser = argparse.ArgumentParser(description="Fast TCP Port Scanner")
    parser.add_argument(
        "-t",
        "--target",
        required=True,
        dest="target",
        help="Victim target to scan (Ex: -t 192.168.100.1)",
    )
    parser.add_argument(
        "-p",
        "--port",
        required=True,
        dest="port",
        help="Port range to scan (Ex: -p 1-100 or -p 80,443,8080)",
    )
    options = parser.parse_args()

    return options.target, options.port


def create_socket():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1)
    open_sockets.append(s)
    return s


def port_scanner(port, host):

    s = create_socket()
    try:
        s.connect((host, port))
        print(colored(f"\n[+] El puerto {port} esta abierto", "green"))

    except (socket.timeout, ConnectionRefusedError):
        pass
    finally:
        s.close()


def scan_ports(ports, target):
    threads = []

    for port in ports:
        thread = threading.Thread(target=port_scanner, args=(port, target))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()


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
