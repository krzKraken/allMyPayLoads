#!/usr/bin/env python3

""" herencia polimorfirmos ejemplo """

from rich import print


class Dispositivos:

    def __init__(self, modelo):
        self.modelo = modelo

    def escanear_vulnerabilidades(self):
        """Metodo abstracto escanear vulnerabilidades"""
        raise NotImplementedError(
            "Este método debe ser definido en el resto de subclases"
        )


class Ordenador(Dispositivos):

    def escanear_vulnerabilidades(self):
        return f"[+] Analisis de vulnerabilidades concluido en {self.modelo}:  Actualizacion de software necesarias, multiples desactualizaciones de software detectadas"


class Router(Dispositivos):

    def escanear_vulnerabilidades(self):
        return f"[+] Analisis de vulnerabilidades concluido en {self.modelo}: Multiples críticos abiertos, es recomedable cerrar estos puertos"


class Telefono(Dispositivos):

    def escanear_vulnerabilidades(self):
        return f"[+] Analisis de vulnerabilidades concluido en {self.modelo}: Multiples aplicaciones detectada con permisos excesivos"


pc = Ordenador("Dell XPS")
telefono = Telefono("Sangsun s23")
router = Router("huaweey x12")


def detectar_vuls_dispositivos(dispositivos):
    print("[green] funcion polimorfirmo[/green] ")
    print(dispositivos.escanear_vulnerabilidades())


detectar_vuls_dispositivos(pc)
detectar_vuls_dispositivos(telefono)
detectar_vuls_dispositivos(router)
