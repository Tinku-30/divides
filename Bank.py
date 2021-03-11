class Bank:
    def __init__(self):
        self.minimum = 100
        self.balance = 1000
    def get_balance(self):
        return self.balance
    def withdraw(self, amount):
        if amount < self.minimum:
            print("Enter a Minimum of 100")
        elif amount > self.balance:
            print("Insufficient Funds")
        else:
            self.balance = self.balance - amount
            return self.balance


my_account = Bank()
my_account.withdraw(100)
balance = my_account.get_balance()
print(balance)
my_account.withdraw(1250)
balance = my_account.get_balance()
print(balance)
