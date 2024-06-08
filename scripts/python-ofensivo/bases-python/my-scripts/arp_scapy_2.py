import argparse

from scapy.all import ARP, Ether, srp


def arp_scan(ip_range):
    # Construye el paquete ARP
    arp_request = ARP(pdst=ip_range)
    # Construye el paquete Ethernet
    broadcast = Ether(dst="ff:ff:ff:ff:ff:ff")
    # Combinación de paquetes Ethernet y ARP
    arp_request_broadcast = broadcast / arp_request
    # Envío del paquete y obtención de la respuesta
    answered_list = srp(arp_request_broadcast, timeout=2, verbose=False)[0]
    # Listado de hosts encontrados
    clients = []
    for sent, received in answered_list:
        # Guardamos la IP y MAC address de los hosts encontrados
        clients.append({"ip": received.psrc, "mac": received.hwsrc})

    return clients


def print_clients(clients):
    print("IP Address\t\tMAC Address")
    print("-----------------------------------------")
    for client in clients:
        print(f"{client['ip']}\t\t{client['mac']}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="ARP Scanner using Scapy")
    parser.add_argument("ip_range", help="IP range to scan (e.g., 192.168.1.0/24)")
    args = parser.parse_args()

    # Escanea los hosts
    clients = arp_scan(args.ip_range)
    # Imprime los resultados
    print_clients(clients)
