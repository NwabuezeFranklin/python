# Christmas Recap

num1 = input("Height of tree: ")
num1 = int(num1)
stump = num1 - 1
spaces = num1 - 1
new = 1
while num1 > 0:
    for i in range(spaces):
        print(" ",end="")
    for m in range(new):
        print('#',end="")
    print()
    new += 2
    spaces -= 1
    num1 -=1

for j in range(stump):
    print(" ",end="")
print("#")




