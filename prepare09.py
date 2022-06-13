friend = ""
friendList = []

while friend != "end":
    friend = input("Enter a friend's name: ")
    if friend != "end":
        friendList.append(friend)

print("\nYour friends are: \n" + "\n".join(friendList))
