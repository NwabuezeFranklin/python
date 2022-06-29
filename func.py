# the numbers entered should be able to increment and should be greater than 1
m,j = input('Enter two numbers and get prime numbers within the range: ').split()
m = int(m)
j = int(j)
if m > 1 & m < j:
    for n in range(m,j+1):
        for i in range(2,n):
            if n % i == 0:
                break
        else:   
            print(n)
else:
    print('Read Instructions again')

    


