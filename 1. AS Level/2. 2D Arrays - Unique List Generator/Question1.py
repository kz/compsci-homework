# Question 1
# Author: Kelvin Zhang
# Date Created: 2015-11-16

import random

"""
Helper functions
"""


def unique_list_generator():
    """
    Generates a list of six unique, randomly chosen integers between 1 and 49 in ascending order
    :return: random_list
    """
    random_list = []
    for i in range(0, 6):
        while True:
            rand_int = random.randint(1, 49)
            if rand_int in random_list:
                continue
            else:
                random_list.append(rand_int)
                break

    # Sort list into ascending order
    random_list.sort()

    return random_list


"""
Main code
"""

# Generate random list to compare against
masterList = unique_list_generator()

# Output master list to user
print("Initial list of numbers:")
print(masterList)

# Count the loops needed to generate the same set of numbers in the master list
loopsMade = 0
while True:
    loopsMade += 1

    if masterList == unique_list_generator():
        break

# Output the number of loops made to user
print("{!s} loops were made to match the list of numbers.".format(loopsMade))
