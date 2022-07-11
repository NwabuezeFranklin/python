def factorial(num):
    if (num == 1) or (num == 0):
        return 1
    else:
        num = num * factorial(num - 1)
        return num

num = int(input("Enter a number"))
for i in range(num):
    current  = factorial(i)
    print("The factorial of {} is {}".format(i,current))