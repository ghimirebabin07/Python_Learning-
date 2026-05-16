# ATM - PIN + Balance + Transaction History

class atmsystem:
    def __init__(self, owner, balance, pin):
        self.owner = owner
        self.balance = balance
        self.pin = pin
        self.history = []

    def deposite(self, amount):
        self.balance += amount
        self.history.append(f"Deposited {amount}")
        print("New Balance:", self.balance)

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            self.history.append(f"Withdraw {amount}")
            print("New Balance:", self.balance)
        else:
            print("Insufficient Balance!")

    def checkbalance(self):
        print("Current Balance:", self.balance)

    def showhistory(self):
        print("\n--- Transaction History ---")
        if not self.history:
            print("No transactions found.")
        else:
            for transaction in self.history:
                print(transaction)


atm = atmsystem("Babin", 2000, "2065")

attempts = 3

while attempts > 0:
    pin = input("Enter the PIN: ")

    if pin == atm.pin:
        print("Login Successful!")
        break
    else:
        attempts -= 1
        print("Invalid PIN! Attempts left:", attempts)

if attempts == 0:
    print("Account Locked!")
    exit()

while True:
    print("\n==== ATM OPTIONS ====")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Show History")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        amt = int(input("Enter the deposit amount: "))
        atm.deposite(amt)

    elif choice == "2":
        amt = int(input("Enter the withdraw amount: "))
        atm.withdraw(amt)

    elif choice == "3":
        atm.checkbalance()

    elif choice == "4":
        atm.showhistory()

    elif choice == "5":
        print("Thanks for using the ATM system.")
        break

    else:
        print("Invalid choice!")