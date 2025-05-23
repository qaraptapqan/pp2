class Bank:
    def __init__(self, owner: str, balance: int):
        self.owner = owner
        self.balance = balance
    def deposit(self, dep_sum):
        if dep_sum < 0: raise ValueError("User can not add negative sum to balance")
        self.balance += dep_sum
    def withdraw(self, wdr_sum):
        if wdr_sum < 0: raise ValueError("User can not withdraw negative sum from balance")
        if wdr_sum > self.balance: raise ValueError("Withdraw sum exceed balance/limit")

        self.balance -= wdr_sum
    def __repr__(self) -> str:
        return f'{self.owner = } {self.balance = }'


loliki = Bank("Chapan", 1000000)
print(loliki)
loliki.deposit(1000)
print(loliki)
loliki.withdraw(500000)
print(loliki)
try:
    loliki.withdraw(600000)
except ValueError:
    print("Couldn't wihdraw 600,000")
    print(loliki)
loliki.deposit(13213123213)
print(loliki)
