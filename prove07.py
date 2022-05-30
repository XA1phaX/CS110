from Lists.words import words
import random

# Intro message
print("\nWelcome to the word guessing game!\n\n")

# Setting up vairables
secretWord = random.choice(words)
guess = ""
guess_count = 0

# Run the game
while guess != secretWord:
    guess = input("Guess a word: ")
    guess_count += 1
    if guess == secretWord:
        print(f"\nYou guessed correctly! It took you {guess_count} tries.\n")
    else:
        print("\nSorry, that's not it.\n")
