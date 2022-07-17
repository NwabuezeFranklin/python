import random

frank = {"person1":"James", "person2":"Rodriguez"}
for keys in frank:
    print(keys, frank[keys])

list1 = [1,2,3,4,5,6,7,8,9]

print([i for i in [ random.randint(1,1000)for x in  range(10)] if i % 9 == 0])
print([i * 2 for i in range(11) if i % 2 != 0])
lis1 = list(random.randint(1,1000) for i in range(50))
print([i for i in lis1 if i % 9 == 0])
print([i ** 2 for i in list1 if i % 2 == 1])