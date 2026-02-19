class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.__balance = balance  # “private-ish”

    def deposit(self, amount):
        self.__balance += amount

    def get_balance(self):
        return self.__balance
    
    def balance(self):
        return f"Balance is {self.__balance}"

    

   
accounts = BankAccount("kunal",200)
print(accounts.get_balance())
# accounts.__balance = 999999 
# print(accounts.get_balance())
