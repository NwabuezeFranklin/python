invested, interest = input('Enter amount invested + interest rate: ').split()
invested = int(invested)
interest = int(interest)

interest = (interest/100) * invested
#  Earnings of a 10 year period
print('Earnings for a 10 year period {}'.format(interest * 10))
