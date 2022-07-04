def prime(num):
    for i in range(2,num):
        if num % i == 0:
            return False
    else:
        return True

def listthe(num1):
    list1 = []
    for i in range(2,num1):
        if prime(i):
            list1.append(i)
    return list1

list1 = int(input('Enter a max number to get a return of prime within: '))
list = listthe(list1)
for prime in list:
    print(prime)


