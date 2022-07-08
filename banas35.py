list = 'abcdefgt'
i = len(list)-1
print(i)
crypto = ''
list1 = []
list3 = list1

while i > 0:
    list3 = list1
    for m in list:
        if m == list[-1]:
            break

        list1.append(m)
        print(m,end="")
    print()
    for m in list3:
        if m == list3[-1]:
            break
        print(m,end="")
    break








