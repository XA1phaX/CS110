words = []
with open("listword.txt", "r") as f:
    for line in f:
        words.append(line.strip())
