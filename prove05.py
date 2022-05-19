from Classes.pretty import *

# Setup pretty import
color = colorClass()


# Function Setup


def remove(string):
    return "".join(string.split())


def error():
    print(
        f"\n{color.RED()}{color.BOLD()}ERROR:{color.END()} Choice invalid. Please restart game. Make sure spelling is correct and\
 you have not added spaces."
    )
    quit()


# Welcome message
print("")
print("─" * 65)
print(f"\nWelcome to {color.RED()}'A Night In The Woods'{color.END()} by JT\n")
print(
    "In this game, you will be given a prompt and asked to make a choice between 2 options."
)
print(
    f"The available options will be {color.CYAN()}{color.UNDERLINE()}UNDERLINED{color.END()}, colored and captialized as such."
)
print("The choices you make will lead to different outcomes. Have fun! - JT\n")
print("─" * 65)

# Starting Question
answer1 = input(
    f"\nYou are out camping deep in the woods and plan to stay for 3 days, you just arrived and\nhave 5 hours\
 until sundown do you {color.CYAN()}{color.UNDERLINE()}EXPLORE{color.END()} or {color.CYAN()}{color.UNDERLINE()}SETUP{color.END()} camp?\n"
)

# Remove Spaces
answer1 = remove(answer1)

# Decision 1
if answer1.lower() == "explore":
    path = 1
elif answer1.lower() == "setup":
    path = 2
else:
    error()

# Decision 2

if path == 1:
    p1_answer1 = input(
        f"\nYou start heading north away from where you plan to camp. You realize that you have\
lost your way!\nYou scavenge around for your compass. You realize you lost it with some other basic supplies!\
\ndo you {color.CYAN()}{color.UNDERLINE()}RETURN{color.END()} or make {color.CYAN()}{color.UNDERLINE()}CAMP{color.END()} here for the night?\n"
    )
if path == 2:
    p2_answer1 = input(
        f"\nIt takes you about an hour to find the perfect spot. You begin setting up camp. After 2 hours, your camp \nis\
setup and you notice you have about 2 hours until sundown. Do you get {color.CYAN()}{color.UNDERLINE()}FIREWOOD{color.END()} or do you\
{color.CYAN()}{color.UNDERLINE()}EXPLORE{color.END()}?\n"
    )

# Exit text
print(
    f"\nThank you for playing! The text game is still {color.UNDERLINE()}Under Development{color.END()} but will be completed soon! Check back in about a week!"
)
