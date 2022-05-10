import math

#Welcome message
print("\nWelcome to the velocity calculator. Please enter the following:\n")

#Recieving inputs
mass = float(input("Mass (in kg): "))
gravity = float(input("Gravity (in m/s^2, 9.8 for Earth, 24 for Jupiter): "))
time = float(input("Time (in seconds): "))
density = float(input("Density of the fluid (in kg/m^3, 1.3 for air, 1000 for water): "))
cross_section = float(input("Cross sectional area (in m^2): "))
drag = float(input("Drag constant (0.5 for sphere, 1.1 for cylinder): "))

#Conversion
c = (1 / 2) * density * cross_section * drag
velocity = math.sqrt((mass * gravity) / c) * (1 - math.exp((-math.sqrt (mass * gravity * c) / mass) * time))

#Output
print(f"\nThe inner value of c is: {c:.3f}")
print(f"\nThe velocity after {time} seconds is {velocity:.3f} m/s")
answer = input("\nWould you like to know the terminal velocity? ")

#Terminal Velocity
if(answer[0] == "y"):
    v_terminal = math.sqrt((mass * gravity) / c)
    print(f"\nTerminal velocity for object: {v_terminal:.3f} m/s")