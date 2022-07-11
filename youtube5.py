class Dog:
    def __init__(self, name, heigth, age):
        self.name = name
        self.heigth = heigth
        self.age = age

    def bark(self):
        print("{} can't bark".format(self.name))

    def run(self):
        print("{} cannot run".format(self.name))

    def strength(self, age, heigth):
        print("{} is {} strong".format(self.name, self.age * self.heigth))
    def printname(self):
        namer = self.name

def  gain():
    secu = Dog('Secu', 5 , 7)
    secu.bark()
    secu.strength(5,7)


gain()

b1 = Dog('leo', 6, 2)
print(b1.bark())
print(b1.strength(6,2))