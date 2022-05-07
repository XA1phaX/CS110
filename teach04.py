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
print(f"The inner value of c is: {round(c, 3)}")
print(f"The velocity after {time} seconds is {round(velocity, 3)} m/s")

#Terminal Velocity
v_terminal = math.sqrt((mass * gravity) / c)
print(f"Terminal velocity for object: {round(v_terminal, 3)} m/s")
