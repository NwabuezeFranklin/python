import math;
#i = [i for i in range(10)]

list = [x for x in range(10)]
print(list)

list1 = [x for x  in range(11) if x % 2 == 1 & x != 0 ]

list2 =[i for i in range(11) if i % 2 == 0]

list1 += list2 # list1.extend(list2)

print(list1)

list3 = [y**2 for y in range(11) if y % 2 == 0]
print(list3)
for i in list3:
    print(i, end=" ")

list4 = [23,45,65,43,23]
print(22 not in list4)
