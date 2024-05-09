class Device:
    def __init__(self, device_type, ip, mac_addrees):
        self.device_type = device_type
        self.ip = ip
        self.mac_addrees = mac_addrees

    def __str__(self) -> str:
        return f"[+] Device ({self.device_type}) - IP: {self.ip} - mac addres {self.mac_addrees}"

    def __repr__(self):
        return self.__str__()
