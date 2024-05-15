#!/usr/bin/env python3
""" vulns scanner """
import os
import re

from devices_class import Device

device_list = []

IP_TEMP_FILE_NAME = "temp_ip_file.txt"


def whats_is_my_ip(file_name):
    os.system(f"ip a > {file_name}")


def capture_my_ip():
    with open(
        IP_TEMP_FILE_NAME,
        "r",
    ) as file:
        text = file.read()
    pathern = r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}"
    ip = re.findall(pathern, text)
    print(ip)


def search_for_devices(ip_range):
    # TODO: Function to search alive device
    ip_range = int(input("[+] Ingrese rango a escanar:"))
    for i in range(ip_range):
        device_list.append(Device("PC", f"192.168.100.{i}", "00:00:00:00:00"))


def main():
    """Main function"""
    # device1 = Device("pc", "192.168.0.100", "00:a1:00:00:00")
    # print(device1)
    # search_for_devices(10)
    whats_is_my_ip(IP_TEMP_FILE_NAME)
    capture_my_ip()


if __name__ == "__main__":
    main()
