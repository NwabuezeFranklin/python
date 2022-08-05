import time
import threading

class bankAccount(threading.Thread):
    balance = 0
    def __init__(self, name, amount,):
        threading.Thread.__init__(self)
        self.name = name
        self.amount = amount
    def run(self):
        threadLock.acquire()
        bankAccount.executing(self)
        threadLock.release()
    def deposit(Amt):
        bankAccount.balance += Amt
        print("Your account just got credited with {} at {}\n The current balance of the Joint account is {}".format(Amt,time.strftime("%H:%M:%S", time.gmtime()),bankAccount.balance))
        time.sleep(1)
        print()

    @staticmethod
    def executing(customer):
        print("{} tries to withdraw {} at {}".format(customer.name,customer.amount,time.strftime("%H:%M:%S", time.gmtime())))
        if bankAccount.balance < customer.amount:
            print("Insufficient Funds")
            print("Account Balance = {}".format (bankAccount.balance))
        elif bankAccount.balance >= customer.amount:
            bankAccount.balance -= customer.amount
            print("{} just withdrew {} by {} ".format(customer.name,customer.amount, time.strftime("%H:%M:%S", time.gmtime())))
            print("Current balance = {}".format(bankAccount.balance))

threadLock = threading.Lock()
t4 = bankAccount.deposit(100000)
t2 = bankAccount("Franklin", 40000)
t1 = bankAccount("Nkechi", 100000)
t3 = bankAccount("Chiboy", 50000)

t2.start()
t1.start()
t3.start()

t2.join()
t1.join()
t3.join()