import os

hrList = {}

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

with open(os.path.join(__location__, "hr_system.txt"), "r") as f:
    for line in f:
        key, value = line.split()
        hrList[key] = value

print(hrList)
