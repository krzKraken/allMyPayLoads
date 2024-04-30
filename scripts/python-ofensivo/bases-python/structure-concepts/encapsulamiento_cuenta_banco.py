#!/urs/bin/env python3
""" Ejemplo encapsulamiento cuenta bancaria """

from rich import print


class CuentaBancaria:
    def __init__(self, cuenta, nombre, saldo_inicial=0):
        self.cuenta = cuenta
        self.nombre = nombre
        self.__saldo = saldo_inicial

    def depositar(self, valor):
        self.__saldo += valor
        print(
            f"[green][+][/green] El usuario {self.nombre} ha depositado {valor} y su saldo disponible es: [orange]{self.__saldo}[/orange]"
        )

    def retirar(self, valor):
        if valor <= self.__saldo:
            self.__saldo -= valor
            print(
                f"[green][+][/green] El usuario {self.nombre} ha retirado {valor} y su saldo disponible es: [orange]{self.__saldo}[/orange]"
            )
        else:
            print(f"[red][-] Saldo insufuciente...[/red]")

    def consultar_saldos(self):
        print(
            f"[green][+][/green] El saldo en la cuenta de {self.nombre} es [orange]{self.__saldo}[/orange]"
        )


manolo = CuentaBancaria("123412", "Manolo Castro")
manolo.depositar(500)
manolo.retirar(200)
manolo.consultar_saldos()
manolo.retirar(1999)
