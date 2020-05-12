class bankAccount():
    # Initializing the class
    def __init__(self):  # Main Method
        self.balance = 0  # Generating Objects

    # This function takes amount you put in as deposit
    def deposit(self, amount):
        self.balance = self.balance + amount

    # This function takes withdraw amount to withdraw from balance
    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance = self.balance - amount
        else:
            print("Insufficient Funds")

    def print_balance(self):
        return self.balance


account = bankAccount()  # Instance of a Class bankAccount
account.deposit(100)
account.deposit(200)
account.deposit(300)
# print(account.print_balance())
account.withdraw(350)
print(account.print_balance())
