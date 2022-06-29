
import random
number1 = 2
number = random.randint(-10, 10)
if number > 0:
    print( f"{number1:d} {number:d}is positive")
elif number == 0:
    print(f"{number:d} is zero")
else:
    print(f"{number:d} is negative")