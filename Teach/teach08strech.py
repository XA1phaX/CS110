sentance = "In coming days, it will not be possible to survive spiritually without the guiding, directing, comforting,\
 and constant influence of the Holy Ghost."
playagain = "y"
i = 0

while playagain[0] == "y":
    number = int(input("Please enter a number: "))
    for i, letter in enumerate(sentance):
        if i % number == 0:
            print(letter.upper(), end="")
        else:
            print(letter, end="")

    playagain = input("\nDo you want to play again (y/n)? ")
    if playagain[0] == "n":
        print("Goodbye")
        break
