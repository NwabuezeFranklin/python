i = 1
while i <= 20:
    if(i % 2) == 0:
        i += 1
        continue
    elif i == 17:
        break
    print('Odd numbers ',i)
    i += 1

