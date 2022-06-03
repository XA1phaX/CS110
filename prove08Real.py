from os import system, name
from Lists.words import *
from Classes.pretty import *
import random

# Imports ^^^

# Setting up vairables
color = colorClass()
playagain = "y"
secretWord = ""
letterCount = 0
guess = ""
guess_count = 0
i = 0
hint = []
correct = []
difficulty = ""


# Functions

# Sets up secret word depending on user input.
def wordDifficulty():
    secretWord = ""
    wordDif = input(
        f"\nWhat word difficulty would you like to play on? {color.GREEN()}EASY{color.END()},\
 {color.BLUE()}Medium{color.END()}, {color.RED()}Hard{color.END()}, or {color.RED()}{color.BOLD()}EXTREME{color.END()}? "
    )
    wordDif = wordDif.lower()
    if wordDif == "easy":
        secretWord = random.choice(easy)
        return secretWord
    elif wordDif == "medium":
        secretWord = random.choice(medium)
        return secretWord
    elif wordDif == "hard":
        secretWord = random.choice(hard)
        return secretWord
    elif wordDif == "extreme":
        secretWord = random.choice(extreme)
        return secretWord
    else:
        secretWord = random.choice(words)
        return secretWord


# Sets difficulty and calls wordDifficulty().
def difficultyFunc():
    # Sets difficulty as global and declares global variables.
    global guess_count
    global difficulty
    global secretWord
    global letterCount
    # Asks user for difficulty.
    difficulty = input(
        f"Choose a difficulty level: \n{color.GREEN()}EASY{color.END()} (100 guesses & free hints!), {color.BLUE()}MEDIUM{color.END()}\
(12 guesses & hints|Hints cost 1 guess!|), \nor {color.RED()}HARD{color.END()} (7 guesses |No hints|): "
    )
    # Sets difficulty to lowercase.
    difficulty = difficulty.lower()
    # If user chooses easy difficulty.
    if difficulty == "easy":
        # Sets number of guesses to 100.
        guess_count = 100
        # Sets secret word to wordDifficulty().
        secretWord = wordDifficulty()
        #
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
    # If user chooses medium difficulty.
    elif difficulty == "medium":
        guess_count = 12
        secretWord = wordDifficulty()
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
    # If user chooses hard difficulty.
    elif difficulty == "hard":
        guess_count = 7
        secretWord = wordDifficulty()
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
    # If user does not correctly enter difficulty.
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
        secretWord = random.choice(extreme)
    letterCount = len(secretWord)


# Checks if letters guessed are in 'correct' list.
def checkCorrectList(letter):
    if letter in secretWord:
        if letter in correct:
            return
        else:
            correct.append(letter)
    else:
        return


# Clears terminal screen.
def clear():

    # For Windows users.
    if name == "nt":
        _ = system("cls")

    # For Mac and Linux(here, os.name is 'posix').
    else:
        _ = system("clear")


# Function to reset variables and lists. Restarts game.
def reset():
    # Runs clear() function.
    clear()
    # Sets variables as global.
    global secretWord
    global letterCount
    global guess
    global guess_count
    global i
    global hint
    global correct
    global letter
    global difficulty
    # Sets variables to default values.
    secretWord = ""
    guess = ""
    difficulty = ""
    guess_count = 0
    i = 0
    hint = []
    correct = []
    # Tells user the game has restarted.
    print(f"\n{color.GREEN()}The word has been reset!{color.END()}")
    # Displays commands.
    print(
        "\nCommands:\nIf you would like to give up at anytime, type 'giveup'\
    If you would like to see\nthe hint at anytime, and are on Easy or Medium difficulty, type 'hint'\n"
    )
    # Runs difficulty() function.
    difficultyFunc()
    # Updates hint with correct list length
    for letter in secretWord:
        hint.append("_")
    # Displays first hint.
    print(f"Your hint is: " + " ".join(hint) + "\n")


# Game loop starts(line 223) because playagain is set to true.


# Intro message.
print("-" * 50)
print(
    "\nWelcome to the word guessing game!\nCommands:\nIf you would like to give up at anytime, type 'giveup'\n\
If you would like to see the hint at anytime, and are on Easy or Medium difficulty, type 'hint'\n"
)
difficultyFunc()
for letter in secretWord:
    hint.append("_")
print("-" * 50)
print(f"\nYour hint is: " + " ".join(hint) + "\n")

# Run the game.
while playagain == "y":
    while guess != secretWord:
        # Check number of guesses left and play again.
        if guess_count <= 0:
            print(f"You ran out of guesses! The word was {secretWord}! You lost.")
            playagain = input("Would you like to play again? (y/n): ").lower()
            if playagain == "y":
                reset()
            else:
                quit()
        # Main game loop.
        else:
            print(f"Guesses left: {guess_count}")
            guess = input("Guess a word: ")
            guess = guess.lower()
            guess_count -= 1
            hintUpdated = []
            # Reset hint
            for letter in secretWord:
                hintUpdated.append("_")
            # Check if user guessed correct word and play again.
            if guess == secretWord:
                print(
                    f"You guessed correctly! The word was {secretWord}! You had {guess_count} guesses left!"
                )
                playagain = input("Would you like to play again? (y/n): ").lower()
                if playagain == "y":
                    reset()
                else:
                    quit()
            # Check if user gave up on current word and play again.
            elif guess == "giveup":
                print(f"The word was {secretWord}! You lost.")
                playagain = input("Would you like to play again? (y/n): ").lower()
                if playagain == "y":
                    reset()
                else:
                    quit()
            # Check if user wants a hint.
            elif guess == "hint":
                hintLetter = ""
                a = 0
                # Easy difficulty hint.
                if difficulty == "easy":
                    hintLetter = random.choice(secretWord)
                    while hintLetter in correct and len(correct) <= len(secretWord):
                        hintLetter = random.choice(secretWord)
                        a += 1
                        if a >= 30:
                            print(
                                "No more hints available! (There are multiples of some letters!)"
                            )
                            break
                    print(f"\nYour hint is: " + " ".join(hintLetter) + "\n")
                    guess_count += 1
                # Medium difficulty hint.
                elif difficulty == "medium":
                    hintLetter = random.choice(secretWord)
                    while hintLetter in correct and len(correct) < len(secretWord):
                        hintLetter = random.choice(secretWord)
                        a += 1
                        if a <= 30:
                            print(
                                "No more hints available! (There are multiples of some letters!)"
                            )
                            break
                    print(
                        f"\nYour hint is: "
                        + " ".join(hintLetter)
                        + "\nThat cost 1 guess!\n"
                    )
                # Hard difficulty hint.
                elif difficulty == "hard":
                    print(f"Hard mode has no hints!")
                # Cheater hint
                else:
                    print(f"You think we would give you a hint? HA!\n")
                    print(
                        f"{color.RED()}{color.BOLD()}C\nH\nE\nA\nT\nE\nR\n!{color.END()}"
                    )
                    quit()
            # Check guess letters declaring variable 'i' and updating hint.
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
                        checkCorrectList(letter)
                        hintUpdated.append(letter.lower())
                i = 0
                # Displays all corect letters guessed
                if difficulty == "easy" or difficulty == "medium":
                    print(
                        f"\nLetters you guessed that are in the answer: "
                        + " ".join(correct)
                    )
                # Prints new hint
                print(f"\nYour hint is: " + " ".join(hintUpdated) + "\n")
