#recieve input of fahrenheit
fahrenheit = float(input("What is the tempeture in Fahrenheit? "))

#conversion
celcius = (fahrenheit - 32) * (5/9)

#output
print(f"The tempeture in celcius is {round(celcius, 1)} degrees.")