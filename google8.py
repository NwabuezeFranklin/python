def factorial(n):
    result = 1
    for x in range(1,n):
        result = result * x
    return result

for n in range(0,9):
    print(n, factorial(n+1))