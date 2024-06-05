import math

def calculate_volume_of_sphere(radius):

    if radius < 0:
        raise ValueError("Radius cannot be negative")
    return (4/3) * math.pi * radius**3