total = 1
j = 0

for i in range(1,10):
    for j in range (1,i):
         total = total * j
    print ( "{} {}".format(j,total))
    total = 1

print(5*4*3*2*1)


def factorial(n):
    result = 1
    for x in range(1,n):
        result = result * x
    return result

for n in range(0,9):
    print(n, factorial(n+1))