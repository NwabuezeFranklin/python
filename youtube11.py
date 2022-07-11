class human:
    num = 0
    def __init__(self, name=""):
        self.name = name
        human.num += 1

    @staticmethod
    def numOfHumans():
        print("There are {} persons".format(human.num))
def main():
    person = human("frank")
    person1 = human("Isdore")
    person2 = human("")
    print(person.name)
    person.numOfHumans()

main()

