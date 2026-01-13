# Write a Python class named Circle constructed by a radius
# and twomethods which will compute the area and the
# perimeter of a circle

import math  # To use the value of pi

class Circle:
    def __init__(self, radius):
        self.radius = radius  

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius

circle1 = Circle(5)
circle2 = Circle(7)

print(f"Circle1 -> Area: {circle1.area():.2f}, Perimeter: {circle1.perimeter():.2f}")
print(f"Circle2 -> Area: {circle2.area():.2f}, Perimeter: {circle2.perimeter():.2f}")
