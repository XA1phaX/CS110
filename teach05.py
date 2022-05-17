# Get input
x = 0
while x < 6:

    grade = float(input("\nWhat is your grade percentage? "))

    # Find letter grade(if-else)

    if grade >= 90:
        letter = "A"
    elif grade >= 80:
        letter = "B"
    elif grade >= 70:
        letter = "C"
    elif grade >= 60:
        letter = "D"
    elif grade < 60:
        letter = "F"
    else:
        letter = "ERROR"

    # Find prefrix
    if (
        ((grade % 10) > 7)
        and (letter != "A")
        and (letter != "F")
        and (letter != "ERROR")
    ):
        sign = "+"
    elif ((grade % 10) < 3) and (letter != "F") and (letter != "ERROR"):
        sign = "-"
    else:
        sign = ""

    # Output
    print(f"\nYour grade is {sign}{letter}")

    if (letter == "A") or (letter == "B") or (letter == "C"):
        print("Congradulations! You passed!")
    else:
        print("You did not pass, but you will do better next time!")
    x = x + 1
