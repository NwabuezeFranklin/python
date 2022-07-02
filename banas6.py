# interest rate pro
money = input('Enter capital')
interest_rate = input('Enter Interest rate')
money = float(money)
interest_rate = float(interest_rate)
interest_rate = interest_rate/100
for i in range(1):
    money = money + (money * interest_rate)
print('The amount made over 10 years totals {:.3f}'.format(money))