class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner        # public
        self._balance = balance   # protected by convention
        self.__pin = 1234         # private-ish

    def deposit(self, amount):
        self._balance += amount

    def get_balance(self):
        return self._balance

a = BankAccount("kunal",25000000)
a.deposit(3000)
print(a._balance)
# print(a.__pin)
# print(a._BankAccount__pin)