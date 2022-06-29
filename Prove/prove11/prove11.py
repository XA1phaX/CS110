import math

country = []
country_code = []
year = []
lifeExpectancy = []
lowest_life_expectancy = 100
lowest_life_expectancy_year = ""
lowest_life_expectancy_country = ""
lowest_life_expectancy_country_code = ""
highest_life_expectancy = 0
highest_life_expectancy_year = ""
highest_life_expectancy_country = ""
highest_life_expectancy_country_code = ""
interested_countries = []
interested_countries_code = []
interested_life_expectancy = []
interested_highest_life_expectancy = 0
interested_highest_life_expectancy_country = ""
interested_lowest_life_expectancy = 100
interested_lowest_life_expectancy_country = ""
interested_population = 0
world_population = []
world_population_year = []
play_again = "y"

### Functions ###
def reset():
    global interested_countries
    global interested_countries_code
    global interested_life_expectancy
    global interested_highest_life_expectancy
    global interested_highest_life_expectancy_country
    global interested_lowest_life_expectancy
    global interested_lowest_life_expectancy_country
    global interested_population
    global world_population
    global world_population_year

    interested_countries = []
    interested_countries_code = []
    interested_life_expectancy = []
    interested_highest_life_expectancy = 0
    interested_highest_life_expectancy_country = ""
    interested_lowest_life_expectancy = 100
    interested_lowest_life_expectancy_country = ""
    interested_population = 0


# Read file
file = open("life-expectancy.csv")
for line in file:
    LE = line.strip()
    parts = LE.split(",")
    # Save each part into a variable
    country.append(parts[0])
    country_code.append(parts[1])
    year.append(parts[2])
    lifeExpectancy.append(parts[3])
file.close()

with open("WorldPopulation.csv") as f:
    for line in f:
        parts = line.strip().split(",")
        world_population.append(parts[1])
        world_population_year.append(parts[0])

# highest life expectancy
for i in range(1, len(lifeExpectancy)):
    lifeExpectancy[i] = float(lifeExpectancy[i])
    if lifeExpectancy[i] > highest_life_expectancy:
        highest_life_expectancy = lifeExpectancy[i]
        highest_life_expectancy_year = year[i]
        highest_life_expectancy_country = country[i]
        highest_life_expectancy_country_code = country_code[i]


# Lowest life expectancy
for i in range(1, len(lifeExpectancy)):

    lifeExpectancy[i] = float(lifeExpectancy[i])
    if lifeExpectancy[i] < lowest_life_expectancy:
        lowest_life_expectancy = lifeExpectancy[i]
        lowest_life_expectancy_country = country[i]
        lowest_life_expectancy_country_code = country_code[i]
        lowest_life_expectancy_year = year[i]

# Find the earliest year measured
lowestyear = 2022
for i in range(1, len(lifeExpectancy)):
    if int(year[i]) < int(lowestyear):
        lowestyear = year[i]
    else:
        continue

# Welcome message
print("\nWelcome to the World Life Expectancy Calculator!")


# Print overalls
print(
    f"The highest life expectancy overall is {highest_life_expectancy} in {highest_life_expectancy_year} in {highest_life_expectancy_country}"
)

print(
    f"The lowest life expectancy overall is {lowest_life_expectancy} in {lowest_life_expectancy_country} in {lowest_life_expectancy_year}\n"
)

# User Input
while play_again == "y":

    user_input = input("Enter the year of interest: ")

    for i in range(1, len(lifeExpectancy)):
        if user_input == year[i]:
            interested_countries.append(country[i])
            interested_countries_code.append(country_code[i])
            interested_life_expectancy.append(lifeExpectancy[i])
        else:
            continue
    # Find Average Life Expectancy for the year
    if len(interested_life_expectancy) > 0:
        average_life_expectancy = sum(interested_life_expectancy) / len(
            interested_life_expectancy
        )

        print(
            f"\nThe average life expectancy for {user_input} is {average_life_expectancy:.3f}"
        )
    else:
        print("No data for that year")

    # Find highest life expectancy and country for the year
    for i in range(1, len(interested_life_expectancy)):
        if interested_life_expectancy[i] > interested_highest_life_expectancy:
            interested_highest_life_expectancy = interested_life_expectancy[i]
            interested_highest_life_expectancy_country = interested_countries[i]
            interested_highest_life_expectancy_country_code = interested_countries_code[
                i
            ]
        else:
            continue
    # Print highest life expectancy and country for the year
    if len(interested_life_expectancy) > 0:
        print(
            f"The highest life expectancy for {user_input} is {interested_highest_life_expectancy} in {interested_highest_life_expectancy_country}"
        )
    else:
        print("No data for highest life expectancy for that year")

    # Find lowest life expectancy and country for the year
    for i in range(1, len(interested_life_expectancy)):
        if interested_life_expectancy[i] < interested_lowest_life_expectancy:
            interested_lowest_life_expectancy = interested_life_expectancy[i]
            interested_lowest_life_expectancy_country = interested_countries[i]
            interested_lowest_life_expectancy_country_code = interested_countries_code[
                i
            ]
        else:
            continue
    # Print lowest life expectancy and country for the year
    if interested_lowest_life_expectancy != 100:
        print(
            f"The lowest life expectancy for {user_input} is {interested_lowest_life_expectancy} in {interested_lowest_life_expectancy_country}"
        )
    else:
        print("No data for lowest life expectancy for that year")

    # Find the population of the world for the year
    for i in range(1, len(world_population)):
        if user_input == world_population_year[i]:
            interested_population = world_population[i]
        else:
            continue
    interested_population = int(interested_population)
    print(
        f"The population of the world in {user_input} was {interested_population:,}\n"
    )

    # Ask user if they want to play again
    play_again = input("Would you like to enter another year? (y/n) ")
    if play_again == "y":
        reset()
        continue
    else:
        print("Thank you for using the World Life Expectancy Calculator!")
        break
