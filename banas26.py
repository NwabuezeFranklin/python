import math
list1 = [3,2,5,4]
list2 = [[math.pow(m,2), math.pow(m,3),math.pow(m,4)]for m in list1]
for i in list2:
    print(i)
print()