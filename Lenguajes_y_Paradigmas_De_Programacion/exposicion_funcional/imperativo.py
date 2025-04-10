# 🔴 Código imperativo con mutabilidad
class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("Fondos insuficientes")

    def transfer(self, amount, recipient):
        if self.balance >= amount:
            self.balance -= amount
            recipient.balance += amount
        else:
            print("Fondos insuficientes para la transferencia")

# Crear cuentas
alice = BankAccount("Alice", 1000)
bob = BankAccount("Bob", 500)

# Realizar transacciones
alice.deposit(500)
alice.withdraw(300)
alice.transfer(200, bob)

print(vars(alice))  # Mutado
print(vars(bob))    # Mutado
