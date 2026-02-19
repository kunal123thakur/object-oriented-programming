class BankAccount:
    def __init__(self,owner,balance=0):
        self.owner = owner
        self._balance = balance

    def dalo(self,amount):
        self._balance += amount
        return f"₹{amount} added. New balance: {self._balance}"
    
    def nikalo(self,amount):
        if amount<= self._balance:
            self._balance -= amount
            return f"₹{amount} withdrawn. New balance: {self._balance}"
        else:
            return f"insufficient balance Balance:{self._balance}"
    def balance(self):
        return f"balance is {self._balance}"
    
account = BankAccount("kunal",200)
print(account.balance())
print(account.dalo(200))
print(account.balance())
print(account.nikalo(30))
print(account.balance())
# account._balance = 999999 
# print(account.balance())
