# Train more on reduce filter map and lambda
import random

lis1 = list(random.randint(1,100)for i in range(1,11))
print(lis1)
print(list(map((lambda x: x + 1), lis1)))