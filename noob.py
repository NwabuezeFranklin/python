import math, os
print(math.pi)
str1 = "Welcome"
print(id(str1))
print(ord('e'))
print("come" not in str1)
str1 += ' ' +'bro'
print(str1)

s = 'Not'
for b in s:
    print(b, end="foo\n")

print(str1.find('e'))
print(str1.count('e'))
ls = ([34,45,32,23,56,34])
#print( "Hello" + ls[:4])
print(ls[:3])