# Question 1
# Description: Creates a list of lucky numbers and outputs the lucky numbers surrounding the input number
# Author: Kelvin Zhang
# Date Created: 2015-12-22

currentIndex = 1

# Create list which will have non-lucky numbers removed, starting with odd numbers only
listOfNumbers = [x for x in range(0, 10004) if x % 2 == 1]

# Create list containing indices which have been iterated on, starting with 1
iteratedIndices = [1]

# Create list of lucky numbers up to 10003
while currentIndex < 10003:
    # Retrieve the next nth term to use
    for x in listOfNumbers:
        if x > currentIndex:
            currentIndex = x
            break

    # Remove every nth element, where n = currentIndex
    multiplier = 1
    while True:
        try:
            listOfNumbers.pop(currentIndex * multiplier - multiplier)
        except IndexError:
            break
        multiplier += 1

# Prompt user for input
while True:
    inputNum = int(input("Enter a number between 2 and 10,000 inclusive: "))

    if not (2 <= inputNum <= 10000):
        print("Invalid number. Please try again.")
        continue
    else:
        break

# Output the lucky numbers surrounding the input number
for idx, val in enumerate(listOfNumbers):
    if inputNum < val:
        greaterThanNumber = val

        if inputNum == listOfNumbers[idx - 1]:
            lessThanNumber = listOfNumbers[idx - 2]
        else:
            lessThanNumber = listOfNumbers[idx - 1]
        break

print("The lucky number less than the input number is {!s}.".format(lessThanNumber))
print("The lucky number more than the input number is {!s}.".format(greaterThanNumber))


