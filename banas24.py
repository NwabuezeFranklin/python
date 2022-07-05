
import math
def gain():
    shape = input('Enter a particular shape, circle or rectangle: ')
    shape_shifter(shape)

def shape_shifter(shape):
    shape = shape.lower()
    #while True:
    if shape == 'rectangle':
        rectangle()
    elif shape == 'circle':
        circle()
    else:
        gain()

def rectangle():
    length = float(input('Enter the length of the rectangle: '))
    width = float(input('Enter the width of the rectangle: '))
    area = length * width
    print('The length of the rectangle: {:.2f}'.format(area))
def circle():
    radius = float(input('Enter the radius of the Circle: '))
    area = math.pi * (math.pow(radius, 2))
    print('The area of the circle = {:.2f}'.format(area))

gain()