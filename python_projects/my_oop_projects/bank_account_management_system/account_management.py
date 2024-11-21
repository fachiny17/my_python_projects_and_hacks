# Additional features
# print("00. Back")
# print("0. Main")
# addition of PIN


class BankAccount:
    def __init__(self, account_number, owner, bank_name, balance=0):
        self.account_number = account_number
        self.owner = owner
        self.bank_name = bank_name
        self.balance = balance

    # Add buy airtime, buy data, account opening
    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited ${amount}. New balance is ${self.balance}")
        # print("00. Back")
        # print("0. Main")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Debit alert! \nDear {self.owner}, you have successfully withdrawn ${
                  amount}. New balance is ${self.balance}. \nThanks for banking with us.")
        else:
            print(f"Insufficient balance! \nYou cannot withdraw ${
                  amount} because your balance is only ${self.balance}")

    def transfer(self, amount):
        if amount <= self.balance:
            # check for case sensitivity and solve the error using .title()
            print(f"1. Transfer to {self.bank_name}")
            print("2. Transfer to Other Banks")
            # print("00. Back")
            # print("0. Main")
            transfer_to = input("Transfer to: ")
            if transfer_to in ["1", f"Transfer to {self.bank_name}"]:
                print
            self.balance -= amount

    def check_balance(self):
        print(f"Account balance: ${self.balance}")
        # print("00. Back")
        # print("0. Main")


account_number = input("Enter account number: ")
owner = input("Enter your name: ")
bank_name = input("Enter your Bank name: ")
account = BankAccount(account_number, owner)
while True:
    print("\nBank Account Menu")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Check Balanace")
    print("4. Exit")

    choice = input("Enter your choice from the above options: ")

    if choice in ["1", "Deposit"]:
        amount = float(input("Enter amount to deposit: "))
        account.deposit(amount)

    elif choice in ["2", "Withdraw"]:
        amount = float(input("Enter the amount to withdraw: "))
        account.withdraw(amount)

    elif choice in ["3", "Check Balance"]:
        account.check_balance()

    elif choice in ["4", "Exit"]:
        print("Exiting the Bank Account Management System. Thanks for banking with us!")
        break

    else:
        print("Invalid choice. Please choose from the options provided above.")
