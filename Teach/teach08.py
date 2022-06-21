magicWord = "commitment"
favLetter = input("What is your favorite letter? ").lower()

for letter in magicWord:
    if letter == favLetter:
        print("_", end="")
    else:
        print(letter, end="")
