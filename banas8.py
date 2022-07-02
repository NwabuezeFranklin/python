# The pine Christmas tree
# Get the desired height
height = input('Enter the desired height: ')
height = int(height)
spaces = height - 1
hashes = 1
stump_spaces = height - 1
while height > 0:
    for i in range(spaces):
        print(' ', end="")
    for i in range(hashes):
        print('#', end="")
    print()
    if height == 3:
        new_space = height - 1
        for i in range(new_space):
            print(' ',end="")
        print("Merry_Christmas")
    spaces = spaces - 1
    hashes = hashes + 2
    height = height - 1
m = 2
while(m > 0):
    for i in range(stump_spaces):
        print(' ', end="")
    print('##')
    m -= 1




