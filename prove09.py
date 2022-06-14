from Classes.pretty import *

color = colorClass()
# Welcome message
print("Welcome to the Shopping Cart program!")

# Set up
cart = {"item": [], "price": [], "quantity": []}

# Loop
while True:
    # Display actions
    print("\nPlease select one of the following actions:")
    print("1. Add item to cart")
    print("2. View cart")
    print("3. Remove item from cart")
    print("4. Compute total")
    print("5. Quit")
    # Get user input
    action = int(input("\nPlease enter an action: "))
    # Perform action
    if action == 1:
        # Action 1: Add item to cart
        # Get item to add
        item = input("What item would you like to add? ")
        # Get price
        price = float(input("How much does " + item + " cost? "))
        # Get quantity
        quantity = int(input("How many " + item + " would you like to add? "))
        # Add item to cart
        cart["item"].append(item)
        cart["price"].append(price)
        cart["quantity"].append(quantity)
        print(f"{color.GREEN()}{item} added to cart!{color.END()}")

    elif action == 2:
        # View cart
        print("\nYour cart contains:")
        for item in cart:
            print(item, ":", cart[item])
    elif action == 3:
        # Remove item from cart
        item = input("What item would you like to remove? ")
        # Remove item from cart
        cart["item"].remove(item)
        cart["price"].remove(item)
        cart["quantity"].remove(item)
        print(f"{color.GREEN()}{item} removed from cart!{color.END()}")
    elif action == 4:
        # Compute total
        total = 0
        for i in range(len(cart["item"])):
            total += cart["price"][i] * cart["quantity"][i]
        print(f"The total is ${total:.2f}")

    elif action == 5:
        # Quit
        print("Thank you for using the Shopping Cart program!")
        break
    else:
        print(f"{color.RED()}{color.BOLD()}ERROR {color.END()}Invalid action: {action}")
