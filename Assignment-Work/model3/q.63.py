# Write a Python program to calculate surface volume and
# area of acylinder



import math

def cylinder_properties(radius, height):
    """
    Calculate the volume and surface area of a cylinder
    """
    volume = math.pi * radius**2 * height
    surface_area = 2 * math.pi * radius * (radius + height)
    return volume, surface_area

# Input from user
radius = float(input("Enter the radius of the cylinder: "))
height = float(input("Enter the height of the cylinder: "))

# Calculate volume and surface area
volume, surface_area = cylinder_properties(radius, height)

# Display results
print(f"Volume of the cylinder: {volume:.2f}")
print(f"Surface area of the cylinder: {surface_area:.2f}")
