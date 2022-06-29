import math, random
from posixpath import split;

num1, num2 = input('Enter two numbers: ').split()
#conversion
num1 = int(num1)
num2 = int(num2)

#sum
sum = num1 + num2
#difference
diff = num1 - num2
#division
div = num1 / num2
#modulus
per = num1 % num2
#multiplication
mult = num1 * num2

print("{} + {} = {}".format(num1,num2,sum))
print("{} - {} = {}".format(num1,num2,diff))
print("{} / {} = {}".format(num1,num2,div))
print("{} % {} = {}".format(num1,num2,per))
print("{} * {} = {}".format(num1,num2,mult))
