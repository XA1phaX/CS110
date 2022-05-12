#Recieving inputs
print("\nWelcome to the Meal Receipt Calculator!\nPlease eneter the following:\n")
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

print(f"Sub-total: ${groupCost:.2f}")
print(f"Tax: ${tax:.2f}")
print(f"Total: ${total:.2f}")

#Getting pay amount

payment = float(input("What is the payment amount: "))
if(payment < total):
    print("Time to wash some dishes!")
else:
    change = payment - total
    print(f"Change: ${change:.2f}")