#  print odd numbers within 1 - 20
num3, num4 = input("Enter numbers within a range: ").split()

num3 = int(num3)
num4 = int(num4)
for i in range(num3, num4+1):
    if i % 2 == 0:
        continue
    else:
        print("{} an odd number".format(i))