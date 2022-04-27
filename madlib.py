#welcome text
print("\nWelcome to Halloween Madlibs!\n")
print("Please enter the following:\n")
print("For reference:")
print("A 'Noun' is a person, place or thing.")
print("A 'Adjective' is a word used to describe a Noun.")
print("A 'Verb' is an action.\n")

#getting inputs from user

adj1 = input("Adjective: ")
adj2 = input("Adjective: ")
adj3 = input("Adjective: ")
animal = input("Animal: ")
noun1 = input("Noun: ")
adj4 = input("Adjective: ")
food = input("Food: ")
verb = input("Verb: ")
noun2 = input("Noun: ")
adverb = input("Adverb: ")
adj5 = input("Adjective: ")
noun3 = input("Noun: ")
noun4 = input("Noun: ")

#function a/an grammer
def grammerfunc(word):
    if word[0] == 'a' or word[0] =='e' or word[0] == 'i' or word[0] =='o' or word[0] == 'u':
        return "an "

    else:
        return "a "

#print story

print("\nYour story is:\n")
print("One " + adj1 + ", " + adj2 + " night, no stars insight. Thunder roared")
print( (grammerfunc(adj3.lower())) + adj3 + " hello; lightning flashed the trees below. The")
print("sound of a " + animal + " could be heard in the distance.\n")
print("It was Halloween night. I was dressed as " + (grammerfunc(noun1.lower())) + noun1 + ". my bag")
print("was beside me filled with " + adj4 + " "+ food + " that I couldnt wait")
print("to eat.\n")
print("As I " + verb + " up the driveway of a house to trick or treat, I")
print("wonder what type of " + noun2 + " I will get.\n")
print("I ring the doorbell with " + adverb + ".")
print ("It opens with a " + adj5 + " man wearing " + (grammerfunc(noun3.lower())) + noun3 + " looks at me.\n")
print("I scream, 'Trick or treat, smell my " + noun4 + "!'")