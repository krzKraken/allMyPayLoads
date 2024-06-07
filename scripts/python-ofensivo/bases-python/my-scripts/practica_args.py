#!/usr/bin/env python3

import argparse
import signal
import sys
import time


def def_handler(sig, frame):
    print("[+] Saliendo..\n")
    sys.exit(1)


signal.signal(signal.SIGINT, def_handler)


def get_arguments():
    parser = argparse.ArgumentParser(description="practica de argparser")

    parser.add_argument(
        "-s", "--time", required=True, dest="time", help="tiempo de espera"
    )
    parser.add_argument(
        "-t", "--target", required=True, dest="target", help="host target"
    )

    options = parser.parse_args()
    return options.time, options.target


def port_scanner():
    host, time = get_arguments()
    print(f"[+] Los argumentos enviados son: {host}, {time}")


def main():

    time.sleep(3)
    port_scanner()


if __name__ == "__main__":
    main()
