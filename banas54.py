from functools import reduce

import random

list1 =list(random.randint(1,1000) for i in range(1,100))
print(list(filter((lambda x: x % 9 == 0), list1 )))

print(reduce((lambda x,y: x + y), range(1,9)))

print(list(map((lambda x,y: x + y), range(1,9), range(1,9))))