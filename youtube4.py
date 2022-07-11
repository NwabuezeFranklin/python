class BankAccount:

    def __init__(self, name, money):
        self.__name = name
        self.__balance = money

    def deposit(self, money):
        self.__balance += money

    def withdraw(self, money):
        if self.__balance > money:
            self.__balance -= money
            return money
        else:
            return "Insufficient funds"

    def checkbalance(self):
        return self.__balance


b1 = BankAccount('tim', 400)
print(b1.withdraw(500))
b1.deposit(500)
print(b1.checkbalance())
print(b1.withdraw(800))
print(b1.checkbalance())



