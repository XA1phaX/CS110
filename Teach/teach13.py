### Imports ###
from cmath import pi

### Variables ###
playAgain = "y"

### Functions ###
def square(x):
    return x * x


def Recarea(x, y):
    return x * y


def cube(x):
    return x * x * x


def circle(x):
    return pi * x**2


### Main ###
while playAgain == "y":
    print("Welcome to the area calculator!")
    print("Please select a shape to calculate:")
    print("1. Square")
    print("2. Rectangle")
    print("3. Circle")
    print("4. Cube")
    print("5. Quit")
    shape = int(input("Please enter a number: "))
    if shape == 1:
        squarelength = float(
            input("What is the length of a side of the square in centimeters? ")
        )
        squarearea = square(squarelength)
        print(f"The area of the square in square centimeters is: {squarearea}cm^2")
        print(f"The area of the square in square meters is: {squarearea / 10000}m^2")
    elif shape == 2:
        reclength = float(input("What is the length of the rectangle in centimeters? "))
        recwidth = float(input("What is the width of the rectangle in centimeters? "))
        recarea = Recarea(reclength, recwidth)
        print(f"The area of the rectangle in square centimeters is: {recarea}cm^2")
        print(f"The area of the rectangle in square meters is: {recarea / 10000}m^2")
    elif shape == 3:
        circradius = float(input("What is the radius of the circle in centimeters? "))
        circarea = circle(circradius)
        print(f"The area of the circle in squared centimeters is: {circarea}cm^2")
        print(f"The area of the circle in meters is: {circarea /10000}m^2")
    elif shape == 4:
        length = float(input("Please enter a single length value in centimeters: "))
        cube = cube(length)
        print(f"The volume of the cube in cubic centimeters is: {cube}cm^3")
        print(f"The volume of the cube in cubic meters is: {cube / 1000000}m^3")
    elif shape == 5:
        print("Goodbye!")
        playAgain = "n"
