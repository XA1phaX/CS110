from Classes.pretty import *

""" from Classes.format import * """

color = colorClass()
""" remove = edit() """

# Welcome message
print("")
print("─" * 65)
print(f"\nWelcome to {color.RED()}'A Night In The Woods'{color.END()} by JT\n")
print(
    "In this game, you will be given a prompt and asked to make a choice between 2 options."
)
print(
    f"The available options will be {color.UNDERLINE()}UNDERLINED{color.END()} and captialized as such."
)
print("The choices you make will lead to different outcomes. Have fun! - JT\n")
print("─" * 65)

# Starting Question
answer1 = input(
    f"\nYou are out camping deep in the woods, you just arrived and\nhave 5 hours\
 until sundown do you {color.UNDERLINE()}EXPLORE{color.END()} or {color.UNDERLINE()}SETUP{color.END()} camp?\n"
)

""" answer1 = remove.remove(answer) """

if answer1.lower() == "explore":
    path = 1
elif answer1.lower() == "setup":
    path = 2
else:
    print(
        f"{color.RED()}{color.BOLD()}ERROR:{color.END()} Choice invalid. Please restart game. Make sure spelling is correct and\
 you have not added spaces."
    )
