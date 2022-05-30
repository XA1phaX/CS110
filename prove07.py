from Lists.words import words
import random

# Intro message
print("\nWelcome to the word guessing game!\n\n")

# Setting up vairables
secretWord = random.choice(words)
letterCount = len(secretWord)
startingLetter = secretWord[0]
guess = ""
guess_count = 0

# Temporary help texts
print(f"\nThe secret word is {letterCount} letters long.\n")
print(f"The first letter of the secret word is {startingLetter}.\n")

# Run the game
while guess != secretWord:
    guess = input("Guess a word: ")
    guess_count += 1
    if guess == secretWord:
        print(f"\nYou guessed correctly! It took you {guess_count} tries.")
    else:
        print("\nSorry, that's not it.")
