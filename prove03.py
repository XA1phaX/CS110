#Recieving inputs

childmeal = float(input("What is the price of a child's meal? "))
adultmeal = float(input("What is the price of an adult meal? "))
isdrink = input("Would you like any drinks? ")

if((isdrink[0].lower()) == 'y'):
    drinkprice = float(input("What is the cost of a drink? "))
    drinknum = int (input("How many drinks would you like? "))

else:
    drinkcost = 0
    drinknum = 0

childnum = int(input("How many children are there? "))
adultnum = int(input("How many adults are there? "))
salestax = float(input("What is the sales tax rate? "))

#Preform Calculations

childcost = childmeal * childnum
adultcost = adultmeal * adultnum
drinktotal = drinkprice * drinknum
groupcost = childcost + adultcost + drinktotal

#Output

print(f"The sub-total is ${round(groupcost, 2)} before tax.")