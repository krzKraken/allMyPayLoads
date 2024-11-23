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


def convert_to_decimal(ip_bin):
    ip = ip_bin.split(".")
    ip_decimal = [str(int(i, 2)) for i in ip]
    return ".".join(ip_decimal)


def get_network_mask(cidr):
    # INFO: El calculo de la Network Mask se realiza colocando 1 en los bits de las direcciones de red de izq a derecha
    cadena_cidr = ("1" * cidr).zfill(32)
    network_mask = cadena_cidr[::-1]
    net_mask_formated = [
        network_mask[i : i + 8] for i in range(0, len(network_mask), 8)
    ]
    return ".".join(net_mask_formated)


def apply_and_to_binaries(cadena1, cadena2):
    # INFO: El calculo del Network ID es el AND de IP y la Network Mask
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


def get_broadcast(ip_bin, cidr):
    # INFO: El broadcast address reemplaza el numero de bits de host de atras hacia delante en la ip original
    ip_reversed = list(reversed(ip_bin.replace(".", "")))
    host = 32 - cidr
    for i in range(host):
        ip_reversed[i] = "1"
    broadcast_address = "".join(reversed(ip_reversed))
    broadcast_address = ".".join(
        [broadcast_address[i : i + 8] for i in range(0, 32, 8)]
    )
    return broadcast_address


def get_host_min(network_id):
    octetos = network_id.split(".")
    last_octeto = int(octetos[-1], 2)  # convetir decimal el ultimo octeto
    last_octeto += 1
    # Reconstruir la direcccion con el ultimo octeto en binario
    octetos[-1] = bin(last_octeto)[2:].zfill(8)
    return ".".join(octetos)


def get_host_max(broadcast_address):
    octetos = broadcast_address.split(".")
    last_octeto = int(octetos[-1], 2)  # convetir decimal el ultimo octeto
    last_octeto -= 1
    # Reconstruir la direcccion con el ultimo octeto en binario
    octetos[-1] = bin(last_octeto)[2:].zfill(8)
    return ".".join(octetos)


def main():
    input_ip = get_arguments().ip
    if is_valid_ip(input_ip):
        # NOTE: Get ip and CIDR
        ip = input_ip.split("/")[0]
        cidr = int(input_ip.split("/")[1])
        # Convert IP to binary
        ip_bin = convert_to_bin(ip)
        print(f"\n[+] IP: {input_ip}\n")
        print(f"{ip_bin}\t->\t({ip}) IP Original")
        # Get the network mask from CIDR
        network_mask = get_network_mask(cidr)
        print(f"{network_mask}\t->\t({convert_to_decimal(network_mask)}) Network Mask")
        # Get the AND between ip and netmask
        network_id = apply_and_to_binaries(ip_bin, network_mask)
        print(f"{network_id}\t->\t({convert_to_decimal(network_id)}) Network ID")
        broadcast = get_broadcast(ip_bin, cidr)
        print(f"{broadcast}\t->\t({convert_to_decimal(broadcast)}) Broadcast Address")
        # MIn host
        host_min = get_host_min(network_id)
        print(f"{host_min}\t->\t({convert_to_decimal(host_min)}) Host Min")
        host_max = get_host_max(broadcast)
        print(f"{host_max}\t->\t({convert_to_decimal(host_max)}) Host Max")


if __name__ == "__main__":
    main()
