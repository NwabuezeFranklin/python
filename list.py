list1 = [1,2,3,4,5,6,7]
print(list1[2:-3])
list1.append(8)
print(list1)
print(list1.count(2))
list2 = [9,10,11,12]
list1.extend(list2)
print(list1)
list1.insert(0,0)
print(list1)
list1.pop(12)
#print(list1)
#list.remove(functions same as the above)
list3 =[34,12,45,23]
list1.extend(list3)
list1.reverse()
print(list1)
list1.sort()
print(list1)
