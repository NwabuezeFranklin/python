def endless(*args):
    mult = 1
    for i in args:
        mult *= i
    return mult

m = endless(2,3,5,6)
print(m)