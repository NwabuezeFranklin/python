class rectangle:

    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self, length, width):
        area1 = length * width
        return area1
    def perimeter(self, length, width):
        perimeter = (length + width) * 2
        return perimeter

def main():
        r2 = rectangle(34, 45)
        print(r2.area(34,45))
main()

r1 = rectangle(34,45)
print(r1.area(34,45))
print(r1.perimeter(34, 45))