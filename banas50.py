def funcer(name: str, age: int, height:float):
    print(name)
    print(age)
    print(height)
    return "My name is {} I'm {:02d} and {:.2f}ft tall".format(name,age,height)



print(funcer('Franklin',33, 6))
print(funcer.__annotations__)