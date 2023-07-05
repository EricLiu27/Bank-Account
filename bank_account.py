class BankAccount:
    # don't forget to add some default values for these parameters!
    all_account = []
    def __init__(self, int_rate, balance): 
        # your code here! (remember, instance attributes go here)
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.all_account.append(self)
        # don't worry about user info here; we'll involve the User class soon
    def deposit(self, amount):
        # your code here
        self.balance += amount
        return self
    def withdraw(self, amount):
        # your code here
        if self.balance >= amount:
            self.balance -= amount
        elif self.balance < amount:
            print("Insufficient funds: Charging a $5 fee")
            self.balance -= 5
        return self
    def display_account_info(self):
        # your code here
        print(f"Your bank account balance is {self.balance}")
        return self
    def yield_interest(self):
        # your code here
        self.balance = self.balance + (self.balance * self.int_rate)
        return self
    @classmethod
    def all_balances(cls):
        for account in cls.all_account:
            account.display_account_info()




bank_account_eric = BankAccount(.01, 500)
bank_account_tony = BankAccount(.05, 1000)

bank_account_eric.deposit(100).deposit(40).deposit(99).withdraw(400).yield_interest().display_account_info()
bank_account_tony.deposit(500).deposit(600).withdraw(44).withdraw(400).withdraw(999).withdraw(111).yield_interest().display_account_info()

BankAccount.all_balances()