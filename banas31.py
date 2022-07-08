def factorial(num):
    if (num == 1) or (num == 0):
        return 1
    else:
        num = num * (factorial(num - 1))
        return num
m = factorial(5)
print(m)