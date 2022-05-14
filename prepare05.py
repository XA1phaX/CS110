
#First second number assignment 

#Recieve input
numOne = float(input("\nWhat is the first number? "))
numTwo = float(input("What is the second number? "))

#if-else statements
if(numOne > numTwo):
    print("The first number is greater")
else:
    print("The first number is not greater")

if(numOne == numTwo):
    print("The numbers are equal")
else:
    print("The numbers are not equal")

if(numOne < numTwo):
    print("The second number is greater")
else:
    print("The second number is not greater")

#Favorite animal

userFav = input("\nWhat is your favorite animal? ")
if userFav.lower() == "wolf":
    print("That's my favorite animal too!")
else:
    print("That one isn't my favorite.")