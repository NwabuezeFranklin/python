import math
class Square:
    def __init__(self, length=0, heigth=0):
        self.__length = length
        self.__heigth = heigth
    @property
    def heigth(self):
        return self.__heigth
    @heigth.setter
    def heigth(self, value):
        if value.isdigit():
            self.__heigth = value
        else:
            print("Enter a numerical value")

    @property
    def length(self):
        return self.__length
    @length.setter
    def length(self, value):
        if value.isdigit():
            self.__length = value
        else:
            print("Numerical Error")
            main()

    def area(self):
        return int(self.__length) * int(self.__heigth)



def main():
    asquare = Square()
    heigth = input('Enter the heigth of the square: ')
    length = input("Enter the length of the square: ")

    asquare.heigth =  heigth
    asquare.length = length

    print('The height is ', asquare.heigth)
    print("The length is ", asquare.length)
    print("The area of the square: ", asquare.area())

main()




















