import argparse
import re
import signal
import sys


def def_handler(sig, frame):
    print(f"\n\n[!] Exiting...\n\n")
    sys.exit(1)


signal.signal(signal.SIGINT, def_handler)


def get_arguments():
    parser = argparse.ArgumentParser(
        description="Automatic tool to calculate the subnetting from IP/CIDR"
    )
    parser.add_argument(
        "-i",
        "--ip",
        type=str,
        help="IP/CIDR",
        required=True,
    )
    return parser.parse_args()


def is_valid_ip(ip_cidr):
    ip = ip_cidr.split("/")[0]
    cidr = ip_cidr.split("/")[1]
    print(f"\nValidating IP and CIDR...\n")
    regex = (
        r"^(25[0-5]|2[0-4][0-9]|1?[0-9]{1,2})(\.(25[0-5]|2[0-4][0-9]|1?[0-9]{1,2})){3}$"
    )
    if re.search(regex, ip):
        if -1 < int(cidr) < 33:
            print(f"[+] IP is valid...\n")
            return True
        else:
            print(f"\n[-] CIDR is no valid\n")
    else:
        print(f"\n[-] IP no Valid...\n")

        return False


def convert_to_bin(ip):
    ip = ip.split(".")
    ip_bin = [bin(int(i))[2:].zfill(8) for i in ip]
    return ".".join(ip_bin)


def convert_to_hex(ip_bin):
    ip = ip_bin.split(".")
    ip_decimal = [str(int(i, 2)) for i in ip]
    return ".".join(ip_decimal)


def get_network_mask(cidr, name="Network Mask"):
    cadena_cidr = ("1" * cidr).zfill(32)
    network_mask = cadena_cidr[::-1]
    net_mask_formated = [
        network_mask[i : i + 8] for i in range(0, len(network_mask), 8)
    ]
    return ".".join(net_mask_formated)


def apply_and_to_binaries(cadena1, cadena2):
    # Dividir las cadenas en octetos usando el separador .
    octeto1 = cadena1.split(".")
    octeto2 = cadena2.split(".")

    # Aplicar And bit a bit a cada par de octetos
    resultado_octetos = []
    for o1, o2 in zip(octeto1, octeto2):
        # AND bit a bit entre los bits de los octetos
        resultado = "".join(
            "1" if b1 == "1" and b2 == "1" else "0" for b1, b2 in zip(o1, o2)
        )
        resultado_octetos.append(resultado)
    # reunir los octetos en una sola cadena
    return ".".join(resultado_octetos)


def main():
    input_ip = get_arguments().ip
    if is_valid_ip(input_ip):
        # NOTE: Get ip and CIDR
        ip = input_ip.split("/")[0]
        cidr = int(input_ip.split("/")[1])
        # Convert IP to binary
        ip_bin = convert_to_bin(ip)
        print(f"\n[+] IP: {input_ip}\n")
        print(f"{ip_bin}\t->\t({ip})")
        # Get the network mask from CIDR
        network_mask = get_network_mask(cidr)
        print(f"{network_mask}\t->\t({convert_to_hex(network_mask)})")
        # Get the AND between ip and netmask
        network_id = apply_and_to_binaries(ip_bin, network_mask)
        print(f"{network_id}\t->\t({convert_to_hex(network_id)})")

        # TODO: Broadcast addres sustituir los bits de host de atras hacia delante en la network id por 1


if __name__ == "__main__":
    main()
