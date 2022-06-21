from Classes.pretty import *

# Setup pretty import
color = colorClass()


# Function Setup

# Remove spaces function
def remove(string):
    return "".join(string.split())


# Error function
def error():
    print(
        f"\n{color.RED()}{color.BOLD()}ERROR:{color.END()} Choice invalid. Please restart game. Make sure spelling is correct and\
 you have not added spaces."
    )
    quit()


# Exit text function
def exit():
    print(
        f"\nThank you for playing! The text game is still {color.UNDERLINE()}Under Development{color.END()} but will be completed soon! Check back in about a week!"
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
    f"\nYou are out camping deep in the woods and plan to stay for 3 days, you just arrived and\nhave 5 hours \
until sundown. Do you {color.CYAN()}{color.UNDERLINE()}EXPLORE{color.END()} or {color.CYAN()}{color.UNDERLINE()}SETUP{color.END()} camp?\n"
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
        f"\nYou start heading north away from where you plan to camp. You realize that you have \
lost your way!\nYou scavenge around for your compass. You realize you lost it with some other basic supplies!\
\nDo you {color.CYAN()}{color.UNDERLINE()}RETURN{color.END()} or make {color.CYAN()}{color.UNDERLINE()}CAMP{color.END()} here for the night?\n"
    )
    if p1_answer1.lower() == "return":
        # Decision 3
        p1_p1_answer = input(
            f"\nYou begin trying to retrace your steps. The sun is begining to set and off to your left you see a \
cave!\nDo you make camp in the {color.CYAN()}{color.UNDERLINE()}CAVE{color.END()} or do you continue {color.CYAN()}{color.UNDERLINE()}WALKING{color.END()}? \n"
        )
        # Results
        if p1_p1_answer.lower() == "cave":
            print(
                f"\nYou set up camp in the cave and go to sleep. In the night you get mauled by a bear!\n{color.RED()}{color.UNDERLINE()}YOU ARE DEAD{color.END()}"
            )
            exit()
        elif p1_p1_answer.lower() == "walking":
            print(
                f"\nYou continue walking in the direction you think you came from. After 3 hours you find a road and are rescued by a good semeritan!\n\
{color.BLUE()}{color.UNDERLINE()}YOU SURVIVED!{color.END()}"
            )
            exit()
        else:
            error()
    elif p1_answer1.lower() == "camp":
        # Decision 3
        p1_p2_answer = input(
            f"\nYou begin setting up camp. You get your tent and bedding set up right before the sun sets, but you run out of time to \
get firewood before dark!\nDo you get {color.CYAN()}{color.UNDERLINE()}FIREWOOD{color.END()} anyway, or do you go to \
{color.CYAN()}{color.UNDERLINE()}SLEEP{color.END()}? \n"
        )
        # Results
        if p1_p2_answer.lower() == "firewood":
            print(
                f"\nYou get as much firewood as you can before sundown. Luckily tonight is a full moon and you can start your fire.\nAs you sleep \
by your fire, you can hear something moving around but staying out of sight of the fire. \nYou sleep peacefully and find your way back in the morning.\n\
{color.BLUE()}{color.UNDERLINE()}YOU SURVIVED!{color.END()}"
            )
            exit()
        elif p1_p2_answer.lower() == "sleep":
            print(
                f"\nYou go straight to sleep, hoping that your tent is enough to protect you. During the night a large mysterious creature attacks you!\n\
{color.RED()}{color.UNDERLINE()}YOU ARE DEAD{color.END()}"
            )
            exit()
        else:
            error()
    else:
        error()
if path == 2:
    # Decision 2
    p2_answer1 = input(
        f"\nIt takes you about an hour to find the perfect spot. You begin setting up camp. After 2 hours, your camp \nis \
set up and you notice you have about 2 hours until sundown. Do you get {color.CYAN()}{color.UNDERLINE()}FIREWOOD{color.END()} or do you \
{color.CYAN()}{color.UNDERLINE()}EXPLORE{color.END()}?\n"
    )
    # Decision 3
    if p2_answer1.lower() == "firewood":
        p2_p1_answer = input(
            f"\nYou go out and find enough firewood for the night. You decide to cook some food and as you do, a small\n\
creature that you dont recognize comes up and looks at you. Do you {color.CYAN()}{color.UNDERLINE()}GIVE{color.END()} it some of your food or \
{color.CYAN()}{color.UNDERLINE()}NO{color.END()}?\n"
        )
        # Result
        if p2_p1_answer.lower() == "give":
            print(
                f"\nYou give some of your food to the mysterious creature. It seems very happy! He follows you into your tent and snuggles\n\
up next to you for the night!\n{color.BLUE()}{color.UNDERLINE()}YOU SURVIVED! (and made a new friend){color.END()}"
            )
            exit()
        elif p2_p1_answer.lower() == "no":
            print(
                f"\nThe creature becomes visibly angry and turns red! Before you can react, the creature jumps up and attacks your face!\n\
{color.RED()}{color.UNDERLINE()}YOU ARE DEAD{color.END()}"
            )
            exit()
        else:
            error()
    elif p2_answer1.lower() == "explore":
        p2_p2_answer = input(
            f"\nYou begin to explore around. You realize that you are in a forbiden area of the forest!\nYour mother told you that weird things \
happen to people who stay the night in this part of the forest. \nDo you {color.CYAN()}{color.UNDERLINE()}STAY{color.END()} the night or \
do you go {color.CYAN()}{color.UNDERLINE()}HOME{color.END()}? \n"
        )
        if p2_p2_answer.lower() == "stay":
            print(
                f"\nYou decide to stay. You stay up all night watching mysterious creatures come out! All of a sudden an animal you dont recognize becomes agressive!\n\
{color.RED()}{color.UNDERLINE()}YOU ARE DEAD{color.END()}"
            )
            exit()
        elif p2_p2_answer.lower() == "home":
            print(
                f"\nYou pack up your stuff as fast as possible. As you are returning to your car, you see some mysterious lights coming out \n\
of the forest. Good thing you left when you did.\n{color.BLUE()}{color.UNDERLINE()}YOU SURVIVED!{color.END()}"
            )
            exit()
        else:
            error()
    else:
        error()
