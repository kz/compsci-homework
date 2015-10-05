# Question 4
# Author: Kelvin Zhang
# Date Created: 2015-10-15

from math import ceil

MINIBUS_NUM = 3
MINIBUS_CAPACITY = 16

# Prompt for user input
numPupils = int(input("How many pupils are going? "))

# Calculate number of minibuses needed
minibusesNeeded = int(ceil(numPupils / MINIBUS_CAPACITY))

if minibusesNeeded <= MINIBUS_NUM:
    print("There are enough minibuses. {!s} are needed.".format(minibusesNeeded))
else:
    print("There are not enough minibuses needed. The trip cannot happen.")
