from tkinter import Variable

#Recieving Name: takes input, saves as 'name' and responds
name = input ("Hello World, please enter name: ")
print ("Hello,", name)

#Recieving color: takes input, saves as 'color' and responds
color = input ("What is your favorite color? ")
print ("I like", color, "too!")

#Functions

#Function confirming favorite color 
def colorFunc(color2):

    print(color2, "is your favorite color right?")
    answer2 = input ("Enter Y for yes and N for no: ")
    if answer2.upper() == "Y":
        print("Yay! I have a good memory, haha")

    else:
        print("Oh, sorry. My mistake.")
        color2 = input ("So what is your favorite color? ")
        print ("Okay, i'll get it right next time!")
        colorFunc(color2)

#Function confirming name and running color function
def nameFunc(name2, color2):
   ## Asking about Name
    print(name2, "is your name right?")
    answer1 = input ("Enter Y for yes and N for no: ")
    if answer1.upper() == "Y":
        print("Yay! Well very nice to meet you! ")

    else:
        print("Oh, sorry. My mistake.")
        name2 = input ("So what is your name? ")
        print ("Okay,", name2, "i'll get it right next time!")
        colorFunc(color2)


#Run function
nameFunc(name, color)