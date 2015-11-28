# Question 2
# Description: Checks if a 2D array is a latin square
# Author: Kelvin Zhang
# Date Created: 2015-11-28

# Is a latin square
LIST_TO_CHECK = [[1, 2, 3, 4, 5],
                 [2, 3, 4, 5, 1],
                 [3, 4, 5, 1, 2],
                 [4, 5, 1, 2, 3],
                 [5, 1, 2, 3, 4]]

# Is not a latin square
# LIST_TO_CHECK = [[1, 2, 3, 4, 5],
#                   [3, 3, 4, 5, 1],
#                   [3, 4, 1, 1, 2],
#                   [4, 5, 1, 2, 3],
#                   [5, 1, 2, 3, 5]]

# Check if the list is square
listLength = len(LIST_TO_CHECK)
if not all(len(row) == listLength for row in LIST_TO_CHECK):
    print("The list is not a square list.")
    exit()

# Check if the list's values meet the conditions to be a latin square
maxValue = len(LIST_TO_CHECK)
possibleValues = [x + 1 for x in range(0, maxValue)]

# Iterate through each row, checking to see if each row fulfils the conditions for a latin square
for row in range(0, len(LIST_TO_CHECK)):
    possibleValuesForRow = possibleValues.copy()

    for column in range(0, len(LIST_TO_CHECK[row])):
        currentValue = LIST_TO_CHECK[row][column]
        if currentValue in possibleValuesForRow:
            possibleValuesForRow.remove(currentValue)
        else:
            print("The list is not a latin square.")
            exit()

# Iterate through each column, checking to see if each column fulfils the conditions for a latin square
for column in range(0, listLength):
    possibleValuesForColumn = possibleValues.copy()

    for row in range(0, len(LIST_TO_CHECK)):
        currentValue = LIST_TO_CHECK[row][column]
        if currentValue in possibleValuesForColumn:
            possibleValuesForColumn.remove(currentValue)
        else:
            print("The list is not a latin square.")
            exit()

# Output to user
print("This list is a latin square.")
