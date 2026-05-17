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
        interest = self.balance *self.interest_rate
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
        print(f"Minimum Balance: Rs.{self.minumum_balance}")
        





