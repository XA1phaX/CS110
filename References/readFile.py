import os

# Set directory location
__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

# Open file
with open(os.path.join(__location__, "wordstext.txt"), "r") as f:
    # Read file
    words = f.readlines()
