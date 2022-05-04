#Recieving inputs

childMeal = float(input("What is the price of a child's meal? "))
adultMeal = float(input("What is the price of an adult meal? "))
isDrink = input("Would you like any drinks? ")

if((isDrink[0].lower()) == 'y'):
    drinkPrice = float(input("What is the cost of a drink? "))
    drinkNum = int (input("How many drinks would you like? "))

else:
    drinkPrice = 0
    drinkNum = 0

childNum = int(input("How many children are there? "))
adultNum = int(input("How many adults are there? "))
salesTax = float(input("What is the sales tax rate? "))

#Preform Calculations

childCost = childMeal * childNum
adultCost = adultMeal * adultNum
drinkTotal = drinkPrice * drinkNum
groupCost = childCost + adultCost + drinkTotal
tax = (groupCost * salesTax) / 100
total = groupCost + tax
#Output

print(f"Sub-total: ${round(groupCost, 2)}")
print(f"Tax: ${round(tax, 2)}")
print(f"Total: ${round(total, 2)}")

#Getting pay amount
payment = float(input("What is the payment amount: "))
if(payment < total):
    print("Time to wash some dishes!")
else:
    change = payment - total
    print(f"Change: {round(change, 2)}")