class User(object):
    def __init__(self, name, balance, checking_account):
        self.name = name
        self.balance = balance
        self.checking_account = checking_account
    
    def withdraw(self, money):
        if self.balance - money < 0: raise(ValueError)
        self.balance -= money
        return f"{self.name} has {self.balance}."
    
    def check(self, user, money):
        if user.balance < money or not user.checking_account: raise(ValueError)
        self.balance += money
        user.balance -= money
        return f"{self.name} has {self.balance} and {user.name} has {user.balance}."
    
    def add_cash(self, money):
        self.balance += money
        return f"{self.name} has {self.balance}."
    