import math
import random

class Bank:
    def __init__(self,name="", money=0):
        self.__money = money
    def setMoney(self,money):
        self.__money = money
    def deposit(self, money):
        self.__money += money
    def withdraw(self,money):
        if money >= self.__money:
            print("Insufficient Funds")
        else:
            self.__money - money
            return self.__money
    def checkbalance(self):
        return self.__money
def main():
    Arinze = Bank("Arinze", 500)
    Arinze.deposit(1000)
    Arinze.checkbalance()
    print(Arinze.checkbalance())
    print(Arinze.withdraw(2000))


main()
