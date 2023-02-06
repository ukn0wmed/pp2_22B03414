import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def show(self):
        print("The coordinates of the point are: ({}, {})".format(self.x, self.y))

    def move(self, delta_x, delta_y):
        self.x += delta_x
        self.y += delta_y

    def dist(self, second_point):
        return math.sqrt((self.x - second_point.x)**2 + (self.y - second_point.y)**2)


pointcoords = Point(4, 5)
pointcoords.show()
pointcoords.move(3, 4)
pointcoords.show()
secondpoint = Point(10, 8)
print(pointcoords.dist(secondpoint))
