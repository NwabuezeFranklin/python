def finobacci(num):
    if num == 0:
        return 0
    elif num == 1:
        return 1
    else:
        result = finobacci(num - 1) + finobacci(num - 2)
        return result

num1 = 23
i = 1
while i <= num1:
    f = finobacci(i)
    print(f)
    i+=1
print('AllDone')
