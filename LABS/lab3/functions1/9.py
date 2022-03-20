import math

class Shape:
    class Sphere:
        def __init__(sphere, radius):
            sphere.radius = radius
        
        def Volume(sphere):
            print("The volume of a sphere is:", math.pi * (4 / 3) * pow(sphere.radius, 3))

if __name__ == "__main__":
    r = int(input("Enter the radius: "))
    Shape().Sphere(r).Volume()