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
hintUpdated = hint
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
    hintUpdated = []
    for letter in secretWord:
        hintUpdated.append("_")
    if guess == secretWord:
        print(
            f"You guessed correctly! The word was {secretWord}! It took you {guess_count} tries."
        )
    else:
        for letter in guess:
            if i < letterCount:
                if letter in secretWord:
                    if letter == secretWord[i]:
                        hintUpdated[i] = letter.upper()
                        i += 1
                    else:
                        hintUpdated[i] = letter.lower()
                        i += 1
                else:
                    hintUpdated[i] = "_"
                    i += 1
            else:
                hintUpdated.append(letter.lower())
        i = 0
        print(f"\nYour hint is: " + " ".join(hintUpdated) + "\n")
