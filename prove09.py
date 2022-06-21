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
    action = input("\nPlease enter an action: ")
    try:
        action = int(action)
    except ValueError:
        print(
            f"\n{color.RED()}{color.BOLD()}ERROR{color.END()}: Please enter an action number"
        )
        continue
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
        # print cart items, prices, and quantities
        for i in range(len(cart["item"])):
            print(
                f"Item {i+1}: {cart['item'][i]} - ${cart['price'][i]:.2f} x {cart['quantity'][i]}"
            )

        # for item in cart:
        #     print(item, ":", *cart[item])
    elif action == 3:
        # Remove item from cart
        item = input("What item would you like to remove? ")
        for i in range(len(cart["item"])):
            if cart["item"][i] == item:
                cart["item"].pop(i)
                cart["price"].pop(i)
                cart["quantity"].pop(i)
                print(f"{color.GREEN()}{item} removed from cart!{color.END()}")
                break
    elif action == 4:
        # Compute total
        total = 0
        tax = 0
        for i in range(len(cart["item"])):
            total += cart["price"][i] * cart["quantity"][i]
        tax = total * 0.085
        print(f"The total is ${total:.2f}")
        print(f"The tax is ${tax:.2f}")
        print(f"The total with tax is ${total + tax:.2f}")

    elif action == 5:
        # Quit
        print("Thank you for using the Shopping Cart program!")
        break
    else:
        print(f"{color.RED()}{color.BOLD()}ERROR {color.END()}Invalid action: {action}")
