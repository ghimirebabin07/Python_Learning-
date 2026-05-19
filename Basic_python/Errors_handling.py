class InsufficientFundsError(Exception):
    def __init__(self,balance,amount):
        super().__init__(f"Cannot withdraw Rs. {amount}. Avilable:Rs.{balance}")

class NegativeAmountError(Exception):
    def __init__(self):
        super().__init__(f"Amount must be greater than zero.")

class MinimumBalanceError(Exception):
    def __init__(self,minimum):
        super().__init__(f"Balance cannot go below Rs.{minimum}")


class Bankaccount:
    def __init__(self,owner,balance=0):
        self.owner = owner 
        self.balance = balance 

    def deposite(self,amount):
        try:
            if amount <=0:
                raise NegativeAmountError()
            self.balance += amount 
            print(f"Deposited Rs.{amount}. Balance: Rs.{self.balance}")
        except NegativeAmountError as e:
            print(f"{e}")
    
    def withdraw(self,amount):
        try:
            if amount <=0:
                raise NegativeAmountError()
            if amount > self.balance:
                raise InsufficientFundsError(self.balance , amount )
            self.balance -= amount 
            print(f"Withdraw Rs.{amount}.Balance: Rs.{self.balance}")
        except(NegativeAmountError, InsufficientFundsError) as e:
            print(f"{e}")
    
    def get_details(self):
        print(f"Owner :{self.owner}")
        print(f"Balance: Rs.{self.balance}")
        print(f"Type : {type(self).__name__}") 


class SavingAccount(Bankaccount):
    def __init__(self,owner,balance=0, interest_rate=0.5):
        super().__init__(owner, balance)
        self.interest_rate = interest_rate
        self.minimum_balance = 500
    
    def withdraw(self, amount ):
        try:
            if amount <=0:
                raise NegativeAmountError()
            if self.balance - amount < self.minimum_balance:
                raise MinimumBalanceError(self.minimum_balance)
            self.balance -= amount 
            print(f"Withdraw Rs.{amount}.Balance: Rs.{self.balance}")
        except(NegativeAmountError, MinimumBalanceError) as e:
            print(f"{e}")
    
    def add_interest(self):
        interest = self.balance * self.interest_rate
        self.balance += interest 
        print(f"Interest Rs. {interest:2f} added. Balance: Rs.{self.balance:2f}")
        
print("="*45)
print("         TESTING ERROR HANDLING ")
print("="*45)

acc = SavingAccount("Babin",balance=20000)
acc.get_details()

print("\n---Normal Operation---")
acc.deposite(500)
acc.withdraw(300)

print("\n--Triggering errors---")
acc.deposite(-100)
acc.withdraw(0)
acc.withdraw(2000)

print("\n ---Interest--")
acc.add_interest()


         