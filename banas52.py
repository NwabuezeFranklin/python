import random

list1 = []
for i in range(1,101):
    list1 += random.choice(['H', 'T'])

print("Heads : ", list1.count('H'))
print("Tails : ", list1.count('T'))
