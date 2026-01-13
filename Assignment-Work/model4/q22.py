# Write a Python class named Circle constructed by a radius
# and twomethods which will compute the area and the
# perimeter of a circle

import math

class Circle :
    def __init__(self,redius):
        self.redius = redius
    def area(self):
        return math.pi*self.redius**2
    def perimeter (self):
        return 2*math.pi*self.redius
    

circle1 = Circle(5)
circle2 = Circle(7)


print("Circle1: Area =", round(circle1.area(), 2), 
      "Perimeter =", round(circle1.perimeter(), 2))