#!/usr/bin/env python3

import argparse
import re
import signal
import subprocess
import sys
from concurrent.futures import ThreadPoolExecutor, thread

from termcolor import colored

"""
Escaner de equipos por traza ICMP
"""


def def_handler(sig, frame):
    print(colored("[+] Saliendo...\n\n", "red"))
    sys.exit(1)


signal.signal(signal.SIGINT, def_handler)


def get_arguments():
    parser = argparse.ArgumentParser(
        description="Tool to discovery active host in a lan using (ICMP)"
    )
    parser.add_argument(
        "-t",
        "--target",
        required=True,
        dest="target",
        help="Host or host range of lan to scann",
    )
    args = parser.parse_args()
    return args.target


def parser_target(targets):

    # target -> 192.168.100.1-100 or 192.168.100.1
    valid_ip = re.match(
        r"^([0-9]{1,3}.){3}(([0-9])||([0-9]{1,3}\-[0-9]{1,3}))$", targets
    )  # Valir ip format
    target_splitted = targets.split(".")  # ['192', '168', '100' , '1-100']
    first_three_octets = ".".join(target_splitted[:3])  # 192.168.1

    if valid_ip:

        if "-" in targets.split(".")[-1]:
            start, end = target_splitted[3].split("-")

            if all(map(lambda octet: int(octet) < 256, target_splitted[:3])):
                print(
                    colored(
                        f"[+] El target {targets}, is valid and is a range {start},{end}",
                        "green",
                    )
                )
                return [
                    f"{first_three_octets}.{i}" for i in range(int(start), int(end) + 1)
                ]
            else:
                return []
        else:
            print(colored(f"[!] The target {targets} is valid and is one IP", "green"))
            return [targets]
    else:
        print(colored(f"[!] The target {targets} is not valid", "red"))
        sys.exit(1)


def host_discovery(target):
    try:
        print(f"pingando a {target}")
        ping = subprocess.run(
            ["ping", "-c", "1", target], timeout=3, stdout=subprocess.DEVNULL
        )
        if ping.returncode == 0:
            print(colored(f"\t[i] The host {target} is active", "green"))
    except subprocess.TimeoutExpired:
        pass


def main():
    target_str = get_arguments()
    targets = parser_target(target_str)
    print(colored(f"[+] Listing active host on {target_str} ", "yellow"))

    # NOTE: Using threadings
    max_threadings = 50
    with ThreadPoolExecutor(max_workers=max_threadings) as excecutor:
        excecutor.map(host_discovery, targets)


if __name__ == "__main__":
    main()
