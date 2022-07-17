# The function of functions
def sum(num):
    summer = 0
    for i in range(num):
        summer += i
    return summer
def returner(sum,nummer):
    return sum(nummer)

def crazy(returner,sum,num):
    return returner(sum,num)

we = returner(sum,34)
print(we)
nume = 4
me = sum(nume)
print(me)

me = crazy(returner,sum, 4)
print(me)