# Author: Kelvin Zhang
# Date Created: 2016-10-11
# Last Modified: 2016-10-11

import math

# There are two parts to this program: working out the cost; recording the students who
# are going and whether they have paid; working out the final costs

# Working out the cost
# ====================
# We must add the cost of the coach ($550) to $30 * num of students
# However, we must take away $30 for every ten students since every tenth students
# receives a free ticket. Alternatively, we can use a for loop over the n students
# and every tenth loop, we do not add $30. We will use the former method.

# First, we prompt for the number of students and ensure this value is greater than 1
numStudents = int(input("Enter the number of students: "))
if not numStudents >= 1:
    print("You must enter 1 or greater")
    exit()

# We set the initial total cost to the cost of the coach
totalCost = 550
# Next, we add on the cost of the students without the discount
totalCost += numStudents * 30
# Finally, we calculate how many times to take away $30 for the discount by dividing
# by 10 and rounding down; there are many ways to divide and round down, but we will
# do this by importing the math package.
numDiscounts = math.floor(numStudents / 10)
totalCost -= numDiscounts * 30

# Finally, we must output the recommended cost per student by dividing the total cost
# by the number of students and rounding this up to the nearest integer
recommendedTicketPrice = math.ceil(totalCost / numStudents)
# {!s} casts whatever is input to .format(...) to a string and embeds it in the string
print("The recommended ticket price is ${!s}".format(recommendedTicketPrice))

# Recording the students
# ======================
# To do this, we will prompt input for each student using a for loop and store the data
# into a single array (containing [name, paid]) like in the following example:
# [["Steve", true], ["Ben", false], ["Kevin", true]]
# Therefore, index 0 is the name and index 1 is the payment status boolean
# Next, we will loop through the array to create two arrays based on payment status

# Prompt input
students = []
for i in range(0, numStudents):
    studentName = input("Enter the name of student #{!s}: ".format(i + 1))
    studentHasPaid = input("Has the student paid? [y/n]: ")

    if studentHasPaid == "y" or studentHasPaid == "Y":
        studentHasPaid = True
    else:
        studentHasPaid = False

    students.append([studentName, studentHasPaid])

# Find which students have and have not  paid
paidStudents = []
notPaidStudents = []
# Loop through the students list
for student in students:
    # Check whether the student has paid is True
    if student[1]:
        # Append the name of the student to paidStudents
        paidStudents.append(student[0])
    else:
        notPaidStudents.append(student[0])

# Print out the students who have and have not paid
print("The following students have paid: ", paidStudents)
print("The following students have not paid: ", notPaidStudents)

# Work out final costs
# ====================
# To work out whether the school has made a profit, loss or broken even,
# we will work out the total income and subtract the total costs

# Find the total number of students who have paid
totalPaid = len(paidStudents) * recommendedTicketPrice
# Find the net income
netIncome = totalPaid - totalCost

print("The total of the costs is ${!s} and the money collected is ${!s}.".format(totalCost, totalPaid))

# Output whether the school trip has made a profit, loss or broken even
if totalPaid == totalCost:
    print("The school trip has broken even.")
elif totalPaid > totalCost:
    print("The school trip has made a profit.")
else:
    print("The school trip has made a lost.")