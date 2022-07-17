def odd(num):
    if num % 2 == 0:
        return False
    else:
        return True

def list(lister, func):
    lister1 =[]
    for i in lister:
        if not func(i):
            lister1.append(i)
    return lister1

list1 = range(1,20)

print(list(list1,odd))