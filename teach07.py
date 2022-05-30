import random

playagain = "yes"
magic = 0
guess = 0
count = 0
while playagain == "yes":
    magic = random.randint(1, 100)
    guess = 0
    count = 0
    while guess != magic:
        guess = int(input("Guess the magic number: "))
        if guess < magic:
            print("Too low")
            count += 1
        elif guess > magic:
            print("Too high")
            count += 1
        else:
            print("You got it!")
            count += 1
            print(f"You guessed {count} times")
    playagain = input("Do you want to play again? ")
