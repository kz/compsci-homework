# Question 2
# Author: Kelvin Zhang
# Date Created: 2015-10-15

from datetime import datetime

from dateutil.relativedelta import relativedelta


# Prompt for initial user input
gameAmount = int(input("How many games has the player played? "))

if gameAmount < 50:
    # Prompt for join date
    joinDate = datetime.strptime(input("When did the player join the club? [dd/mm/yyyy] "), '%d/%m/%Y')

    # Calculate whether player is beginner or improver
    if joinDate > datetime.now() - relativedelta(None, None, 1):
        print("The player is a beginner.")
    else:
        print("The player is an improver.")
else:
    # Prompt for average score
    avgScore = int(input("What is the player's average score? "))

    # Calculate whether player is improver or pro
    if avgScore < 180:
        print("The player is an improver.")
    else:
        print("The player is a pro.")
