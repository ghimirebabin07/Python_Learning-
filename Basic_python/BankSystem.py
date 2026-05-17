class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposite(self,amount ):
        if amount <=0:
            print("Deposited amount must be positive")
            return 

        self.balance +=amount
        print(f"Deposited.{amount} New Balance: Rs.{self.balance}")
    
    def withdraw(self,amount):
        if amount <=0:
            print("Withdraw amount must be positive")
            return
        if amount > self.balance:
            print(f"Insufficient funds. Current balance: Rs.{self.balance}")
            return 
            self.balance -=amount
            print(f"Withdraw. {amount} Remaining Balance: Rs. {self.balance}")
    def getdetails(self):
        print(f"Account owner : {self.owner}")
        print(f"Balance Details: Rs{self.balance}")
        print(f"Account type :{type(self).__name__}")


#inheritance concept :
class SavingsAccount(BankAccount):
    def __init__(self, owner , balance=0, interest_rate=0.5):
        super().__init__(owner,balance)
        self.interest_rate = interest_rate
        self.minumum_balance = 500 #specific rule for saving account 
    
    def add_interest(self):
        interest = self.balance * self.interest_rate
        self.balance +=interest 
        print(f"Interest added : Rs.{interest:2f}. New Balance: Rs.{self.balance:2f}")

#overriding 
    def withdraw(self,amount):
        if amount <=0:
            print("Withdraw amount must be positive.")
            return
        
        if self.balance-amount <self.minumum_balance:
            print(f"Cannot withdraw. Minimum balance of Rs.{self.minumum_balance} must remain.")
            print(f"Current balance: Rs.{self.balance} - Max you can withdraw :Rs.{self.balance-self.minumum_balance}")
            return
        super().withdraw(amount)
    
    def getdetails(self):
        super().getdetails()
        print(f"Interest Rate : {self.interest_rate*100}%")
        print(f"Minimum Balance : Rs.{self.minumum_balance}")

class CurrentAccount(BankAccount):
    def __init__(self,owner,balance=0, overdraft_limit=1000):
        super().__init__(owner,balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self,amount):
        if amount <=0:
            print("withdraw amount must be positive ")
            return 
        if amount < self.balance+self.overdraft_limit:
            print(f"Overdraft limit exceeded")
            print(f"Max you can withdraw: Rs.{self.balance+self.overdraft_limit}")
            return 
        self.balance -=amount 
        if self.balnce < 0:
            print(f"Withdraw Rs.{amount}. Balance is now Rs.{self.balance} (overdraft used)")
        else:
            print(f"Withdraw Rs.{amount}.Remaining Balance: Rs.{self.balance}")
    def getdetails(self):
        super().getdetails()
        print(f"Overdraft limit : Rs.{self.overdraft_limit}")
    

print("="*50)
print("         SAVING ACCOUNT -Babin Ghimire")
print("="*50)

saving = SavingsAccount(owner = "Babin Ghimire",balance=20000,interest_rate=0.5)
saving.getdetails()
print("\n---Transaction---")
saving.deposite(1000)
saving.withdraw(2200)
saving.withdraw(500)
saving.add_interest()


print("\n"+"="*50)
print("      CURRENT ACCOUNT -Bishnu Ghimire")
print("="*50)

current = CurrentAccount(owner="Bishnu Ghimire",balance= 50000,overdraft_limit=1000)
current.getdetails()

print("---Transaction---")
current.deposite(4000)
current.withdraw(2000)
current.withdraw(500)

print("\n "+"="*50)
print("     isinstance() CHECK")
print("="*50)

print(f"saving is SavingAccount? {isinstance(saving,SavingsAccount)}")
print(f"saving is BankAccount? {isinstance(saving,BankAccount)}")
print(f"current is CurrentAccount? {isinstance(current,CurrentAccount)}")
print(f"current is SavingAccount? {isinstance(current,SavingsAccount)}")
    

    

        





