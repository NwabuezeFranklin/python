import random
# Crazy just use list.sort, .pop, .reverse, .insert, .remove
list2 = []
for i in range(0,5):
     list2.append(random.randint(0,10))
print(list2)
for i in list2:
     print(i)
i = len(list2)-1
print('The length of the list ', i)
print()
while i > 1:
     j = 0
     while j < i:
          print(list2[j],list2[j + 1])
          if list2[j] > list2[j + 1]:
               print('switching')
               temp = list2[j]
               list2[j] = list2[j + 1]
               list2[j + 1] = temp
          else:
               print('Not switching')
          j += 1
          print('j was incremented, Trasverser')
          print(list2)
          print()
     print('End of round, len is decremented')
     print()


     i -= 1


print(list2)

