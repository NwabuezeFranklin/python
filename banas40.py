import math
class Circle:
    def __init__(self, radius):
        self.__radius = radius
    def getradius(self, radius):
        self.__radius = radius
        return self.__radius
    def area(self, radius):
        self.__radius = radius
        area1 = math.pi * (self.__radius**2)
        return area1
def main():
    circle1 = Circle(23)
    heigth = 5
    circle1.radius = heigth
    circle1.getradius(45)
    print("The new radius is: ",circle1.getradius(25))
    print("The area is: {:.2f} ".format(circle1.area(25)))
main()