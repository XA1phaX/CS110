#Recieving inputs

childmeal = float(input("What is the price of a child's meal? "))
adultmeal = float(input("What is the price of an adult meal? "))
isdrink = input("Would you like any drinks? ")

if((isdrink[0].lower()) == 'y'):
    drinkprice = float(input("What is the cost of a drink? "))
    drinknum = int (input("How many drinks would you like? "))

else:
    drinkprice = 0
    drinknum = 0

childnum = int(input("How many children are there? "))
adultnum = int(input("How many adults are there? "))
salestax = float(input("What is the sales tax rate? "))

#Preform Calculations

childcost = childmeal * childnum
adultcost = adultmeal * adultnum
drinktotal = drinkprice * drinknum
groupcost = childcost + adultcost + drinktotal
tax = (groupcost * salestax) / 100
total = groupcost + tax
#Output

print(f"Sub-total: ${round(groupcost, 2)}")
print(f"Tax: ${round(tax, 2)}")
print(f"Total: ${round(total, 2)}")

#Getting pay amount
payment = float(input("What is the payment amount: "))
if(payment < total):
    print("Time to wash some dishes!")
else:
    change = payment - total
    print(f"Change: {round(change, 2)}")