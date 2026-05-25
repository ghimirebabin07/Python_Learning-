import json 
import os 

class InsufficientFundsError(Exception):
    def __init__(self,balance, amount):
        super().__init__(f"Cannot withdraw Rs.{amount}. Available: Rs.{balance}")


class NegativeAmountError(Exception):
    def __init__(self):
        super().__init__("Amount must be greater than zero.")


class MinimumBalanceError(Exception):
    def __init__(self,minimum):
        super().__init__(f"Balance cannot go below Rs.{minimum}")


class BankAccount:
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
            print(f" {e}")

    def withdraw(self,amount):
        try:
            if amount <=0:
                raise NegativeAmountError()
            if amount >self.balance:
                raise InsufficientFundsError(self.balance , amount)
            self.balance -= amount 
            print(f"Withdraw Rs.{amount}. Balance: Rs.{self.balance}")
        except (NegativeAmountError,InsufficientFundsError) as e:
            print(f"{e}")

    def get_details(self):
        print(f"Owner : {self.owner}")
        print(f" Balance: Rs.{self.balance}")
        print(f" Type : {type(self).__name__}")

    def to_dict(self):
        return {
            "type": type(self).__name__,
            "owner":self.owner,
            "balance":self.balance

        }
    
    def save(self,filename ="account.json"):
        with open(filename,"w") as f:
            json.dump(self.to_dict(), f, indent=4)
        print(f"Account saved to {filename}")
              


    @staticmethod
    def load(filename="account.json"):
        if not os.path.exists(filename):
            raise FileNotFoundError(f"{filename} not found")

        with open(filename, "r") as f:
            data = json.load(f)

        owner = data.get("owner")
        balance = data.get("balance", 0)
        try:
            balance = float(balance)
            if balance.is_integer():
                balance = int(balance)
        except (TypeError, ValueError):
            balance = 0

        account = BankAccount(owner, balance)
        print(f"Account loaded from {filename}")
        return account



if __name__ == '__main__':
    # Simple demonstration
    acct = BankAccount('Babin', 1000)
    acct.deposite(500)
    acct.withdraw(200)
    acct.get_details()
    acct.save('example_account.json')

    loaded = BankAccount.load('example_account.json')
    loaded.get_details()










