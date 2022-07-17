m = range(1,11)
def twox(num):
     return num * 2
print(list(map(twox, m)))

# map allows us to execute a function on each item on a list.
print(list(map((lambda x: x * 3), m)))

print(list(filter((lambda x: x % 2 == 0), range(1,21))))

# filter is map but selective
#  these tricks works only on lists and tuples