class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self._balance = balance

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, amount):
        if amount < 0:
            raise ValueError("Balance cannot be negative")
        self._balance = amount
a = BankAccount("kunal", 1000)
print(a.balance())      # calls @property getter
a.balance = 2000      # calls @balance.setter
