list1 = [1,23,4,5,6,9]
t1 = (1,3,2,45,65)
print(len(t1), len(list1))
print(min(t1), max(list1))
print(sum(t1), sum(list1))
##list1.sort()
#t1.sort() this attribute is not available to a tuple
list1.extend(t1) #This is where the fun starts :)
list1.sort()
list1.append(0)
list1.insert(9,9)
list1.reverse()
print(list1)

for i in list1:
    print(i * 2, end=", ")