# 🟢 Código funcional con inmutabilidad
from dataclasses import dataclass

@dataclass(frozen=True)
class BankAccount:
    name: str
    balance: float

# Función pura para depositar dinero
def deposit(account, amount):
    return BankAccount(account.name, account.balance + amount)

# Función pura para retirar dinero
def withdraw(account, amount):
    return BankAccount(account.name, account.balance - amount) if account.balance >= amount else account

# Función pura para transferir dinero entre cuentas
def transfer(sender, recipient, amount):
    if sender.balance >= amount:
        return (
            BankAccount(sender.name, sender.balance - amount),
            BankAccount(recipient.name, recipient.balance + amount)
        )
    print("Fondos insuficientes para la transferencia")
    return sender, recipient

# Crear cuentas sin mutarlas
alice = BankAccount("Alice", 1000)
bob = BankAccount("Bob", 500)

# Realizar transacciones de forma pura
alice1 = deposit(alice, 500)
alice2 = withdraw(alice1, 300)
alice3, bob1 = transfer(alice2, bob, 200)

print(alice3)  # Cuenta final de Alice (no mutada)
print(bob1)    # Cuenta final de Bob (no mutada)
