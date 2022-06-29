def ranger(n,m):
    result = 0
    if n > m:
        print("Read the instructions again")
        return 
    for i in range(n,m+1):
        result = result + i
    print(result)
n, m = input('Enter two numbers the first must be lesser than the latter ').split()
n = int(n)
m = int(m)
ranger(n,m)