#!/usr/bin/env python

import argparse
import re
import signal
import subprocess
import sys

from termcolor import colored

"""
Device identifier windows, linux device 
"""


def def_handler(sig, frame):
    print(colored(f"\n\n[!] Exiting....\n\n", "red"))
    sys.exit(1)


signal.signal(signal.SIGINT, def_handler)


def get_arguments():
    parser = argparse.ArgumentParser(
        description="Tool to discovery active hosts and identify OS with ttl proximity"
    )
    parser.add_argument(
        "-t",
        "--target",
        dest="target",
        help="Host or host range of lan to scan",
    )
    parser.add_argument(
        "-d",
        "--dictionary",
        dest="dictionary",
        help="List of IPs",
    )
    options = parser.parse_args()
    return options.target, options.dictionary


def run_command(command):
    try:
        command_output = subprocess.check_output(command, shell=True)
        return command_output.decode()
    except Exception as e:
        print(colored(f"\n[!]Error...{e}\n", "red"))
    return "No value"


def main():

    target, dictionary_file = get_arguments()
    valid_target = re.search(r"[0-9]{1,3}.[0-9]{1,3}.[0-9]{1,3}.[0-9]{1,3}", target)

    print(colored(f"[+] Ip valida encontrada: {valid_target}", "blue"))

    if valid_target:
        command_output = run_command(f"ping -c 1 {target}")
        print(command_output)


if __name__ == "__main__":
    main()
