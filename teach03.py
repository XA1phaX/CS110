from cmath import pi

#Core requirements lines 5-19

#Square
# squarelength = float(input("What is the length of a side of the square? "))
# squarearea = squarelength **2
# print(f"The area of the square is: {squarearea}")

# #Rectangle
# reclength = float(input("What is the length of the rectangle? "))
# recwidth = float(input("What is the width of the rectangle? "))
# recarea = reclength * recwidth
# print(f"The area of the rectangle is: {recarea}")

# #Circle
# circradius = float(input("What is the radius of the circle? "))
# circarea = pi * circradius ** 2
# print(f"The area of the circle is: {circarea}")

#Stretch lines 22-31
# length = float(input("Please enter a single length value: "))
# sarea = length **2
# carea = pi * length ** 2
# cube = length **3
# sphere = (4/3) * pi * length **3

# print(f"A square with that length has an area of: {sarea}")
# print(f"A circle with that radius has an area of: {carea}")
# print(f"A cube with that length has a volume of: {cube}")
# print(f"A sphere with that radius has a volume of: {sphere}")

#----------------------------------------------------------------------------------------------
#Strecth 3 lines 36-67

squarelength = float(input("What is the length of a side of the square in centimeters? "))
squarearea = squarelength **2
print(f"The area of the square in square centimeters is: {squarearea}cm^2")
print(f"The area of the square in square meters is: {squarearea / 10000}m^2")


reclength = float(input("What is the length of the rectangle in centimeters? "))
recwidth = float(input("What is the width of the rectangle in centimeters? "))
recarea = reclength * recwidth
print(f"The area of the rectangle in square centimeters is: {recarea}cm^2")
print(f"The area of the rectangle in square meters is: {recarea / 10000}m^2")


circradius = float(input("What is the radius of the circle in centimeters? "))
circarea = pi * circradius ** 2
print(f"The area of the circle in squared centimeters is: {circarea}cm^2")
print(f"The area of the circle in meters is: {circarea /10000}m^2")

length = float(input("Please enter a single length value in centimeters: "))
sarea = length **2
carea = pi * length ** 2
cube = length **3
sphere = (4/3) * pi * length **3

print(f"A square with that length has an area of: {sarea}cm^2")
print(f"A square with that length has an area of: {sarea / 10000}m^2")
print(f"A circle with that radius has an area of: {carea}cm^2")
print(f"A circle with that radius has an area of: {carea / 10000}m^2")
print(f"A cube with that length has a volume of: {cube}cm^2")
print(f"A cube with that length has a volume of: {cube / 10000}m^2")
print(f"A sphere with that radius has a volume of: {sphere}cm^2")
print(f"A sphere with that radius has a volume of: {sphere / 10000}m^2")
