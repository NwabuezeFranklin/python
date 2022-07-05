import math
def main():
    shape = input('Enter a shape of your choice, (Square, Rectangle, Circle, Triangle): ')
    shapeshifter(shape)
def shapeshifter(shape):
    shape = shape.lower()
    if shape == 'rectangle':
        rectangle()
    elif shape == 'circle':
        circle()
    elif shape == 'square':
        square()
    else:
        main()
def rectangle():
    length = float(input('Enter the length of the rectangle: '))
    width = float(input('Enter the width of the rectangle: '))
    area = length * width
    print('The area of the rectangle is {:.2f}'.format(area))

def square():
    length = float(input('Enter the length of the square: '))
    width = float(input('Enter the width of the square: '))
    area = length * width
    print('The area of the square is {:.2f}'.format(area))

def circle():
    radius = float(input('Enter the radius of the circle: '))
    area = math.pi * (math.pow(radius,2))
    print('The area of the circle is {:.2f}'.format(area))


main()