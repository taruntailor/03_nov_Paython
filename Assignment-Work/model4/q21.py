# Write a Python class named Rectangle constructed by a length
# and widthand a method which will compute the area of a
# rectangle


class ReactAngle :

    def __init__(self,lenght,width):

        self.lenght = lenght
        self.width = width

    def area (self):
        return self.lenght*self.width
    
react1= ReactAngle(3,5)

print("Area of rect1:", react1.area())  # Output: 15

