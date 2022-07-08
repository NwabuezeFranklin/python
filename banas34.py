import random
list = []
for i in range(0,7):
    list.append(random.randint(1,20))
print(list)
i = len(list) - 1
while i > 1:
    j = 0
    while j < i:
        if list[j] > list[j+1]:
            temp = list[j]
            list[j] = list[j+1]
            list[j+1] = temp
        else:
            print()
        j+=1
    i-=1
print(list)



