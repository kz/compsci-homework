# This Python file uses the following encoding: utf-8
# Question 1
# Author: Kelvin Zhang
# Date Created: 2015-10-15

# Prompt for initial user input
initialCost = float(input("What is the initial cost of the flight? £"))
suitcaseWeight = float(input("Enter the weight of your suitcase (kg): "))

totalCost = initialCost

# Calculate the suitcase cost
if suitcaseWeight > 20:
    totalCost += 60
    weightOverage = (suitcaseWeight - 20) // 0.5
    totalCost += weightOverage

# Prompt for and calculate gift cost
while True:
    hasGift = input("Will you buy your partner a gift at the airport? [Y/N] ").upper()

    if hasGift == 'Y':
        while True:
            maintenanceLevel = input("What is the maintenance level of the gift? [low/med/high] ").lower()
            if maintenanceLevel == 'low':
                totalCost += 10
            elif maintenanceLevel == 'medium':
                totalCost += 20
            elif maintenanceLevel == 'high':
                totalCost += 50
            else:
                print("Invalid input. Please try again.")
                continue
            break
        break
    elif hasGift == 'N':
        break
    else:
        print("Invalid input. Please try again.")
        continue

# Prompt for and calculate drink price
drinkNum = int(input("How many drinks will you have at the bar? "))
if drinkNum <= 6:
    totalCost += 6 * drinkNum
else:
    totalCost += 300
    print("A missed flight fee of £300 has been added.")

# Output the total cost of the flight
print("The total cost of the flight is £{:2.2f}".format(totalCost))
