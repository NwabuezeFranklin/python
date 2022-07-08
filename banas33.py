class Dog:

    def __init__(self, name, heigth, weigth):
        self.name = name
        self.height = heigth
        self.weigth = weigth

    def run(self):
        print('{} the dog runs'.format(self.name))

    def eat(self):
        print('{} the dog runs'.format(self.name))

    def bark(self):
        print('{} the dog barks'.format(self.name))

def main():
    spot = Dog("Spot", 66, 26)
    spot.bark()
    spot.run()
    leo = Dog('leo', 67, 23)
    leo.bark()
    leo.run()





main()