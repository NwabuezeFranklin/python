# Generator expressions 'yield'

def prime(num):
    for i in range(2,num):
        if num % i == 0:
            return False
    else:
        return True
def numbers(max_num):
    for i in range(2, max_num):
        if prime(i):
            yield(i)

emp = numbers(20)
print(next(emp))

