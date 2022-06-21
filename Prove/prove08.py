from Lists.words import *
import random

# Intro message
print("\nWelcome to the word guessing game!\n\n")

# Setting up vairables
secretWord = random.choice(words)
letterCount = len(secretWord)
guess = ""
guess_count = 0
i = 0
hint = []
for letter in secretWord:
    hint.append("_")
hintUpdated = []

# Start game
print(f"Your hint is: " + " ".join(hint) + "\n")

# Run the game
while guess != secretWord:
    guess = input("Guess a word: ")
    guess = guess.lower()
    guess_count += 1
    if guess == secretWord:
        print(
            f"You guessed correctly! The word was {secretWord}! \nIt took you {guess_count} tries."
        )
    else:
        for letter in guess:
            if i > letterCount - 1:
                hintUpdated.append(letter.lower())
                i += 1
            else:

                if letter in secretWord:

                    if letter == secretWord[i]:
                        hintUpdated.append(letter.upper())
                        i += 1
                    else:
                        hintUpdated.append(letter.lower())
                        i += 1
                else:
                    hintUpdated.append("_")
                    i += 1
        i = 0
        print(f"\nYour hint is: " + " ".join(hintUpdated) + "\n")
        hintUpdated = []
