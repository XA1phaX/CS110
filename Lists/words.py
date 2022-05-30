import os

words = []

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

with open(os.path.join(__location__, "wordstext.txt"), "r") as f:
    for line in f:
        words.append(line.strip())
