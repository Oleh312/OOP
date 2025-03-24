class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance
    
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"{amount} грн додано. Баланс: {self.balance} грн")
        else:
            print("Сума для депозиту має бути більше 0.")
    
    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"{amount} грн знято. Баланс: {self.balance} грн")
        else:
            print("Недостатньо коштів або невірна сума.")


class Transaction:
    def __init__(self, sender, receiver, amount):
        self.sender = sender
        self.receiver = receiver
        self.amount = amount
    
    def execute(self):
        if self.sender.balance >= self.amount:
            self.sender.withdraw(self.amount)
            self.receiver.deposit(self.amount)
            print(f"Транзакція: {self.amount} грн від {self.sender.owner} до {self.receiver.owner} завершена.")
        else:
            print("Транзакція не можлива. Недостатньо коштів.")

# Приклад використання
acc1 = BankAccount("Олександр", 500)
acc2 = BankAccount("Марія", 300)

transaction = Transaction(acc1, acc2, 200)
transaction.execute()

# Перевірка залишку
print(f"Баланс {acc1.owner}: {acc1.balance} грн")
print(f"Баланс {acc2.owner}: {acc2.balance} грн")

