# Starting comment
print("\nFor all questions, please insert a value between 1-10\n")

# Recieve inputs

loanSize = float(input("How large is the loan? "))
credit = float(input("How good is your credit history? "))
income = float(input("How high is your income? "))
downP = float(input("How large is your down payment? "))

# Calculations
shouldLoan = False

if loanSize >= 5:
    if credit >= 7 and income >= 7:
        shouldLoan = True
    elif (credit >= 7 or income >= 7) and downP >= 5:
        shouldLoan = True
    else:
        shouldLoan = False
else:
    if credit < 4:
        shouldLoan = False
    elif income >= 7 or downP >= 7:
        shouldLoan = True
    elif income >= 4 and downP >= 4:
        shouldLoan = True
    else:
        shouldLoan = False

# Print Result

if shouldLoan == True:
    print("You are approved for the loan!")
else:
    print("You are not approved for the loan, sorry.")
