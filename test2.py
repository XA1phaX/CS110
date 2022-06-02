list = ["aabbccdd"]
print(list[0])

new_strings = []


for string in list:

    new_string = string.replace("a", "1")
    new_strings.append(new_string)

print(new_strings[0])
