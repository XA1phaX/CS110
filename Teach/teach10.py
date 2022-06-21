bankAccount = []
balance = []
numberA = 0
highest = 0
highIndex = -1
index = 0
total = 0

print("\nEnter the names and balances of bank accounts (type: quit when done)")
while True:
    name = input("What is the name of this account: ")
    if name == "quit":
        break
    accountBalance = input("What is the balance: ")
    bankAccount.append(name)
    balance.append(accountBalance)
    numberA += 1
print("\nAccount Information:")
for account in bankAccount:
    i = bankAccount.index(account)
    print(f"{i}. {account} - ${balance[bankAccount.index(account)]}")

for balance in balance:
    total += float(balance)
print(f"\nTotal balance: ${total:.2f}")
print(f"Average balance: ${(total/numberA):.2f}")

highest_name = None
highest_balance = -1

for i in range(len(bankAccount)):
    name = bankAccount[i]
    abalance = float(balance[i])

    if abalance > highest_balance:
        # We have a new highest!
        highest_balance = abalance
        highest_name = name
print(f"Highest balance: {highest_name} - ${highest_balance}")

change_account = "yes"

while change_account == "yes":
    change_account = input("\nDo you want to update an account? ")

    if change_account == "yes":
        index = int(input("What account index do you want to update? "))
        new_amount = float(input("What is the new amount? "))

        balance[index] = new_amount

    # Now print the balances
    print("\nAccount Information:")
    for i in range(len(bankAccount)):
        print(f"{i}. {bankAccount[i]} - ${balance[i]:.2f}")
