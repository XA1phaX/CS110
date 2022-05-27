from Classes.pretty import *

color = colorClass()

# Welcome message
print("\nWelcome to the 'Amusement Park Requirements' program!\n")


# Recieve inputs

ageFirst = int(input("What is the age of the first rider? "))
heightFirst = float(input("What is the height of the first rider? "))
isSecond = input("Is there a second rider (yes/no)? ")

canRide = "Welcome to the ride. Please be safe and have fun!"
noRide = "Sorry, you may not ride."

# If second

if isSecond == "yes":
    ageSecond = int(input("What is the age of the second rider? "))
    heightSecond = int(input("What is the height of the second rider? "))

    # Check Golden
    if ageFirst < 18 and ageFirst >= 12:
        gpass = input("Are you a Golden Pass member (yes/no)? ")
        if gpass == "yes":
            ageFirst = 18
    if ageSecond < 18 and ageSecond >= 12:
        gpass2 = input("Is Rider 2 a Golden Pass member(yes/no)? ")
        if gpass2 == "yes":
            ageSecond = 18

    # Calculations 2 riders:

    if heightFirst < 36 or heightSecond < 36:
        print(noRide)
    elif ageFirst >= 18 or ageSecond >= 18:
        print(canRide)
    elif (ageFirst >= 12 and ageSecond >= 12) and (
        heightFirst >= 52 and heightSecond >= 52
    ):
        print(canRide)
    elif (ageFirst >= 16 and ageSecond >= 14) or (ageSecond >= 16 and ageFirst >= 14):
        print(canRide)
    else:
        print(noRide)

elif isSecond == "no":
    # Check Golden
    if ageFirst < 18 and ageFirst >= 12:
        gpass = input("Are you a Golden Pass member (yes/no)? ")
        if gpass == "yes":
            ageFirst = 18
    # Calculations 1 rider
    if heightFirst < 36:
        print(noRide)
    elif ageFirst >= 18 and heightFirst >= 62:
        print(canRide)
    else:
        print(noRide)
else:
    print(
        f"{color.RED()}ERROR:{color.END()} Please restart program. Make sure all inputs are correct and do not have spaces."
    )
