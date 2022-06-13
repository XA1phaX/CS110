# Start message.
print("Enter a list of numbers, type 0 when finished.")
numbers = []
# While loop to get user input.
while True:
    number = int(input("Enter Number: "))
    if number == 0:
        break
    numbers.append(number)
# Find the sum, average, largest, and smallest numbers
sum = 0
for number in numbers:
    sum += number
average = sum / len(numbers)
largest = numbers[0]
smallest = numbers[0]
for number in numbers:
    if number > largest:
        largest = number
    if number < smallest:
        smallest = number
# Print the results
print("The sum is", sum)
print("The average is", average)
print("The largest number is", largest)
print("The smallest number is", smallest)
list.sort(numbers)
for number in numbers:
    print(number)
