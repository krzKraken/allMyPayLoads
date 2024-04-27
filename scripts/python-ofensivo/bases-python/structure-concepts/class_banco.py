#!/usr/bin/env python3
"""
Programa POO class banco
"""
from rich import print


class CuentaBancaria:

    def __init__(self, accountNumber, name, balance):
        self.name = name
        self.accountNumber = accountNumber
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return f"\n[+] {self.name} has made a deposit of {amount} and now has {self.balance} credits"

    def withdraw(self, amount):
        self.balance -= amount
        return f"[+] {self.name} has made a withdraw of {amount} and now has {self.balance} credits"


cris = CuentaBancaria(accountNumber=123213, name="Cris", balance=0)
print(cris.deposit(199))
print(cris.deposit(299))
print(cris.withdraw(100))
