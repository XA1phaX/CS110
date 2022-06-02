from Lists.words import *
import random

# Intro message
print("\nWelcome to the word guessing game!\n\n")

# Setting up vairables
secretWord = random.choice(words)
letterCount = len(secretWord)
# startingLetter = secretWord[0]
guess = ""
guess_count = 0
i = 0
hint = []
for letter in secretWord:
    hint.append("_")
hintUpdated = []
# Temporary help texts
# print(f"\nThe secret word is {letterCount} letters long.\n")
# print(f"The first letter of the secret word is {startingLetter}.\n")
print(secretWord)
print(f"Your hint is: " + " ".join(hint) + "\n")

# Run the game
while guess != secretWord:
    guess = input("Guess a word: ")
    guess = guess.lower()
    guess_count += 1
    if guess == secretWord:
        print(
            f"You guessed correctly! The word was {secretWord}! It took you {guess_count} tries."
        )
    else:
        for letter in guess:
            while i <= letterCount:
                if letter == secretWord[i]:
                    hint[i] = letter.upper()
                    i += 1
                    break
                elif letter in secretWord:
                    hint[i] = letter.lower()
                    i += 1
                    break
                else:
                    i += 1
                    break
        i = 0
        print(f"\nYour hint is: " + " ".join(hint) + "\n")
