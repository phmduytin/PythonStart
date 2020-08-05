import math


class Shape:
    def Area(self):
        pass

    def periMeter(self):
        pass


class Rectangle(Shape):
    def __init__(self, height, width):
        self.height = height
        self.width = width

    def Area(self):
        return self.height * self.width

    def periMeter(self):
        return (self.height + self.width) * 2


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def Area(self):
        return math.pi * (self.radius ** 2)

    def periMeter(self):
        return math.pi * self.radius * 2


rec = Rectangle(3, 4)
cir = Circle(3)


class Car():
    pass


class BWM(Car):
    pass


car = Car()
bwm = BWM()

Shapes = [rec, cir, car, bwm]

for shape in Shapes:
    print(type(shape).__name__)

    if (shape.__class__.__base__.__name__ == 'Shape'):
        print(" Area: ", shape.Area())
        print(" Perimeter: ", shape.periMeter())

