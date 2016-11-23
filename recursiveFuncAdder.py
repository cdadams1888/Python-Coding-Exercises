# Design a recursive function that returns the sum of a range in a list of integers.
# The recursive function should take three arguments;
# the list name, the start index of the range, and the end index of the range.
# To test your function, make a ten element list of small random integers, all from 1 to 20 inclusive.
# Duplicates are okay. Prompt the user to enter the start and end index for the range.
import random
# Declare an empty list.
listName   = []
# Add ten randon integers with values from 1 to 20 in that list.
while len(listName) < 10:
    listName.append(random.randint(1,20))
# Gather the start value from the user.
startIndex = int(input("Enter the index you would like to start with: "))
# Gather the end value from the user.
endIndex   = int(input("Enter the index you would like to end with: "))
# Define a counter
a       = 0
sumNums = 0
def recursiveFunc(listName, startIndex, endIndex):
    global a
    global sumNums
    while(endIndex > a):
        sumNums += listName[startIndex]
        startIndex += 1
        a += 1
        recursiveFunc(listName, startIndex, endIndex)
    return sumNums
recursiveFunc(listName, startIndex, endIndex)
print(sumNums)
