class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self._balance = balance

    def balance(self):
        return self._balance


a = BankAccount("kunal", 1000)
print(a.balance())      
# a.balance = 2000      # this will not happen
print(a.balance())     