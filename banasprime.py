for i in range(2,21):
    for j in range(2,i):
        if i % j == 0:
            break

    else:
        print(i)