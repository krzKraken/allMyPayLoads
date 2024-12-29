#!/usr/bin/env python

import signal
import sys

from termcolor import colored

from forwardshell import ForwardShell


def def_handler(sig, frame):
    print(colored(f"\n\n[!] Exiting...\n\n", "red"))
    my_forwardshell.remove_data()
    sys.exit(1)


signal.signal(signal.SIGINT, def_handler)


if __name__ == "__main__":
    my_forwardshell = ForwardShell()
    my_forwardshell.run()
