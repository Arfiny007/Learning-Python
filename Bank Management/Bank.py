class banking:
    def __init__(self ,user_name,initial_balance) :
        self.name=user_name
        self.balance=initial_balance

    def deposit(self,amount):
        if amount>0:
            self.balance += amount
            return amount
    def withdraw(self,amount):
        if amount<self.balance :
            self.balance -= amount
            return amount
        else :
            f"insufficient Balance"    
    def get_balance(self):
        return self.balance
    
Arfin =  banking("Arfin",20000)

print(f"Account Name : {Arfin.name}")
print(f"Account Initial Balance : {Arfin.balance}")
print(f"Deposti Balance : {Arfin.deposit(5000)}")
print(f"After Deposit Your Balance is : {Arfin.get_balance()}")
print(f"Withdraw Balance : {Arfin.withdraw(8000)}")
print(f"After Withdraw Your Balance is: {Arfin.get_balance()}")
