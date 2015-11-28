# Question 1
# Description: Creates a ragged array and calculates the sum of values in each column
# Author: Kelvin Zhang
# Date Created: 2015-11-28

import random

# Values of the maximum length and possible width of the multi-dimensional array
MAX_WIDTH = 5
MAX_HEIGHT = 5

# Generate a ragged array
while True:
    raggedArray = []
    valueCounter = 0

    for row in range(0, MAX_HEIGHT):
        raggedArray.append([])

        for column in range(0, random.randint(1, MAX_WIDTH)):
            valueCounter += 1
            raggedArray[row].append(valueCounter)

    # Ensure that the lengths of all rows are not equal
    firstRowLength = len(raggedArray[0])
    if all(len(row) == firstRowLength for row in raggedArray):
        continue
    else:
        break

# Output the array
print(raggedArray)

# Calculate the sum of values in each column
listOfSums = [0 for x in range(0, MAX_WIDTH)]

for row in range(0, len(raggedArray)):
    for column in range(0, len(raggedArray[row])):
        listOfSums[column] += raggedArray[row][column]

# Output the sum of each column to the user
for i in range(0, len(listOfSums)):
    print("Sum of column {!s}: {!s}".format(i + 1, listOfSums[i]))