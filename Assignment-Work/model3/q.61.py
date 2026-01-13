# • Write a Python program to calculate the area of a trapezoid



def trapezoid_area(a, b, h):
    """
    Calculate the area of a trapezoid given bases a, b and height h
    """
    area = 0.5 * (a + b) * h
    return area

# Example usage
base1 = float(input("Enter the first base (a): "))
base2 = float(input("Enter the second base (b): "))
height = float(input("Enter the height (h): "))

area = trapezoid_area(base1, base2, height)
print(f"The area of the trapezoid is: {area}")
