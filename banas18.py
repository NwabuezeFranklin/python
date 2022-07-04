num1 = '4'

def float_it(num1):
    try:
        float(num1)
        return True
    except:
        print('We can\'t convert this')
print('Is num a float ', float_it(num1))
float(num1)
print(num1)
