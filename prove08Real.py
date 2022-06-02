from os import system, name
from Lists.words import *
from Classes.pretty import *
import random

# Setting up vairables
color = colorClass()
playagain = "y"
secretWord = random.choice(words)
letterCount = len(secretWord)
guess = ""
guess_count = 0
i = 0
hint = []
correct = []
difficulty = ""
for letter in secretWord:
    hint.append("_")

# Functions


def difficultyFunc():
    global guess_count
    global difficulty
    difficulty = input(
        f"Choose a difficulty level: \n{color.GREEN()}EASY{color.END()} (1 Million guesses & free hints!), {color.BLUE()}MEDIUM{color.END()} (15 guesses & hints|Hints cost 1 guess!|), \
or {color.RED()}HARD{color.END()} (7 guesses |No hints|): "
    )

    difficulty = difficulty.lower()
    if difficulty == "easy":
        guess_count = 1000000
        print(color.GREEN())
        print(
            r"""
    █████████████████████████
    █▄─▄▄─██▀▄─██─▄▄▄▄█▄─█─▄█
    ██─▄█▀██─▀─██▄▄▄▄─██▄─▄██
    ▀▄▄▄▄▄▀▄▄▀▄▄▀▄▄▄▄▄▀▀▄▄▄▀▀
        """
        )
        print(color.END())
    elif difficulty == "medium":
        guess_count = 15
        print(color.BLUE())
        print(
            r"""
    ███╗░░░███╗███████╗██████╗░██╗██╗░░░██╗███╗░░░███╗
    ████╗░████║██╔════╝██╔══██╗██║██║░░░██║████╗░████║
    ██╔████╔██║█████╗░░██║░░██║██║██║░░░██║██╔████╔██║
    ██║╚██╔╝██║██╔══╝░░██║░░██║██║██║░░░██║██║╚██╔╝██║
    ██║░╚═╝░██║███████╗██████╔╝██║╚██████╔╝██║░╚═╝░██║
    ╚═╝░░░░░╚═╝╚══════╝╚═════╝░╚═╝░╚═════╝░╚═╝░░░░░╚═╝
        """
        )
        print(color.END())
    elif difficulty == "hard":
        guess_count = 7
        print(color.RED())
        print(
            r"""
    .------..------..------..------.
    |H.--. ||A.--. ||R.--. ||D.--. |
    | :/\: || (\/) || :(): || :/\: |
    | (__) || :\/: || ()() || (__) |
    | '--'H|| '--'A|| '--'R|| '--'D|
    `------'`------'`------'`------'
        """
        )
        print(color.END())
    else:
        print(
            "\nYou did not choose a valid difficulty level. You will only have 3 guesses as punishment for your mistake."
        )
        guess_count = 3
        print(
            rf"""{color.RED()}
    ███████████████████████████
    ███████▀▀▀░░░░░░░▀▀▀███████
    ████▀░░░░░░░░░░░░░░░░░▀████
    ███│░░░░░░░░░░░░░░░░░░░│███
    ██▌│░░░░░░░░░░░░░░░░░░░│▐██
    ██░└┐░░░░░░░░░░░░░░░░░┌┘░██
    ██░░└┐░░░░░░░░░░░░░░░┌┘░░██
    ██░░┌┘▄▄▄▄▄░░░░░▄▄▄▄▄└┐░░██
    ██▌░│██████▌░░░▐██████│░▐██
    ███░│▐███▀▀░░▄░░▀▀███▌│░███
    ██▀─┘░░░░░░░▐█▌░░░░░░░└─▀██
    ██▄░░░▄▄▄▓░░▀█▀░░▓▄▄▄░░░▄██
    ████▄─┘██▌░░░░░░░▐██└─▄████
    █████░░▐█─┬┬┬┬┬┬┬─█▌░░█████
    ████▌░░░▀┬┼┼┼┼┼┼┼┬▀░░░▐████
    █████▄░░░└┴┴┴┴┴┴┴┘░░░▄█████
    ███████▄░░░░░░░░░░░▄███████
    ██████████▄▄▄▄▄▄▄██████████
    ███████████████████████████
        """
        )
        print(color.END())
        print(f"{color.RED()}{color.BOLD()}Goodluck{color.END()}\n")


def checkCorrectList(letter):
    if letter in correct:
        return
    else:
        correct.append(letter)


def clear():

    # for windows
    if name == "nt":
        _ = system("cls")

    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system("clear")


def reset():
    clear()
    global secretWord
    global letterCount
    global guess
    global guess_count
    global i
    global hint
    global correct
    global letter
    secretWord = random.choice(words)
    letterCount = len(secretWord)
    guess = ""
    guess_count = 0
    i = 0
    hint = []
    correct = []
    for letter in secretWord:
        hint.append("_")

    print(f"\n{color.GREEN()}The word has been reset!{color.END()}")
    print(
        "\nCommands:\nIf you would like to give up at anytime, type 'giveup'\
    If you would like to see\nthe hint at anytime, and are on a Easy or Medium difficulty, type 'hint'\n"
    )
    difficultyFunc()
    print(f"Your hint is: " + " ".join(hint) + "\n")


# Intro message
print("-" * 50)
print(
    "\nWelcome to the word guessing game!\nCommands:\nIf you would like to give up at anytime, type 'giveup'\n\
If you would like to see the hint at anytime, and are on a Easy or Medium difficulty, type 'hint'\n"
)
difficultyFunc()
print(f"Your hint is: " + " ".join(hint) + "\n")

# Run the game
while playagain == "y":
    while guess != secretWord:
        if guess_count <= 0:
            print(f"You ran out of guesses! The word was {secretWord}! You lost.")
            playagain = input("Would you like to play again? (y/n): ").lower()
            if playagain == "y":
                reset()
            else:
                quit()
        else:
            print(f"Guesses left: {guess_count}")
            guess = input("Guess a word: ")
            guess = guess.lower()
            guess_count -= 1
            hintUpdated = []
            for letter in secretWord:
                hintUpdated.append("_")
            if guess == secretWord:
                print(
                    f"You guessed correctly! The word was {secretWord}! You had {guess_count} guesses left!"
                )
                playagain = input("Would you like to play again? (y/n): ").lower()
                if playagain == "y":
                    reset()
                else:
                    quit()
            elif guess == "giveup":
                print(f"The word was {secretWord}! You lost.")
                playagain = input("Would you like to play again? (y/n): ").lower()
                if playagain == "y":
                    reset()
                else:
                    quit()
            elif guess == "hint":
                if difficulty == "easy":
                    print(
                        f"Your hint is: " + " ".join(random.choice(secretWord)) + "\n"
                    )
                    guess_count += 1

                elif difficulty == "medium":
                    print(
                        f"Your hint is: "
                        + " ".join(random.choice(secretWord))
                        + "\nThat cost 1 guess!\n"
                    )
                elif difficulty == "hard":
                    print(f"Hard mode has no hints!")
                else:
                    print(f"You think we would give you a hint? HA!\n")
                    print(
                        f"{color.RED()}{color.BOLD()}C\nH\nE\nA\nT\nE\nR\n!{color.END()}"
                    )
                    quit()

            else:
                for letter in guess:
                    if i < letterCount:
                        if letter in secretWord:
                            if letter == secretWord[i]:
                                hintUpdated[i] = letter.upper()
                                checkCorrectList(letter)
                                i += 1
                            else:
                                hintUpdated[i] = letter.lower()
                                checkCorrectList(letter)
                                i += 1
                        else:
                            hintUpdated[i] = "_"
                            i += 1
                    else:
                        hintUpdated.append(letter.lower())
                i = 0
                if difficulty == "easy" or difficulty == "medium":
                    print(
                        f"\nLetters you guessed that are in the answer: "
                        + " ".join(correct)
                    )
                print(f"\nYour hint is: " + " ".join(hintUpdated) + "\n")
