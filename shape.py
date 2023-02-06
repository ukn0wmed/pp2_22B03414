class Shape:
    def __init__(self):
        pass

    def area(self):
        return 0


class Square(Shape):
    def __init__(self, length):
        self.length = length

    def area(self):
        return self.length * self.length


class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width


shape = Shape()
print("Shape area:", shape.area())

square = Square(5)
print("Square area:", square.area())

rectangle = Rectangle(4, 5)
print("Rectangle area:", rectangle.area())