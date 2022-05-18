from cgitb import text
from Classes.pretty import *

color = colorClass()


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
    f"\nYou are out camping deep in the woods and plan to stay for 3 days, you just arrived and\nhave 5 hours\
 until sundown do you {color.UNDERLINE()}EXPLORE{color.END()} or {color.UNDERLINE()}SETUP{color.END()} camp?\n"
)

# Decision 1
if answer1.lower() == "explore":
    path = 1
elif answer1.lower() == "setup":
    path = 2
else:
    print(
        f"{color.RED()}{color.BOLD()}ERROR:{color.END()} Choice invalid. Please restart game. Make sure spelling is correct and\
 you have not added spaces."
    )

# Decision 2

if path == 1:
    p1_answer1 = input(
        f"You start heading north away from where you plan to camp. You realize that you have\
     lost your way!\n You scavenge around for your compass. You realize you lost it with some other basic supplies!\
     \ndo you {color.UNDERLINE()}RETURN{color.END()} or make {color.UNDERLINE}CAMP{color.END()} here for the night?\n"
    )
if path == 2:
    p2_answer1 = input(
        f"It takes you about an hour to find the perfect spot. You begin setting up camp. After 2 hours, your camp \nis \
     setup and you notice you have about 2 hours until "
    )
