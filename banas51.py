minus = lambda i,j: i - j
print(minus(10,4))

eligible = lambda age: True if age >= 18  else False

powerlist = [lambda x: x**2, lambda x: x**3, lambda x: x**4]

for i in powerlist:
    print(i(2))