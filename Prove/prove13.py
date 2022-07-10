###Variables###
# Ask user for temperature
temp = float(input("\nWhat is the temperature? "))
# Ask user for Fehrenheit or Celsius
temp_type = input("Farhenheit or Celsius(F/C)? ")


###Functions###
# Create function to Compute wind chill up to 60 mph at 5 degree intervals
def wind_chill(temp, wind_speed):
    wind_chill = (
        35.74
        + 0.6215 * temp
        - 35.75 * (wind_speed**0.16)
        + 0.4275 * temp * (wind_speed**0.16)
    )
    return wind_chill


# Convert Celcius to Fahrenheit
def celcius_to_fahrenheit(temp):
    fahrenheit = (temp * (9 / 5)) + 32
    return fahrenheit


# Convert Celcius to Kelvin
def celcius_to_kelvin(temp):
    kelvin = temp + 273.15
    return kelvin


# Convert Fahrenheit to Celcius
def fahrenheit_to_celcius(temp):
    celcius = (temp - 32) * (5 / 9)
    return celcius


###Main Program###
if temp_type.lower() == "c":
    temp = celcius_to_fahrenheit(temp)
else:
    temp = temp

for i in range(5, 61, 5):
    windchill = wind_chill(temp, i)
    celWindchill = fahrenheit_to_celcius(windchill)
    kelWindchill = celcius_to_kelvin(celWindchill)
    print(
        f"At temperature {temp}{temp_type.upper()}, Wind Chill at {i} mph is {windchill:.2f}F or {celWindchill:.2f}C or {kelWindchill:.2f}K"
    )
