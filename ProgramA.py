# This program should use a main function and another function named makelist as follows:
# in main, generate a random integer that is greater than 5 and less than 13.
# print this number on its own line.
# call the makelist function with the random integer as sole argument.
# inside the makelist function:
# make an empty list.
# use a loop to append to the list a number of elements equal to the random integer argument.
# All new list elements must be random integers ranging from 1 to 100, inclusive. Duplicates are okay.
# return the list to main.
# back in main, catch the returned list and sort it.
# finally, use a for loop to display the sorted list elements,
# all on one line, separated by single spaces.


import random
def main():
    randomInt = random.randint(6,12)
    print(randomInt);
    showList = makelist(randomInt)
    showList.sort()
    for x in range(0,randomInt):
        print(showList[x], end=' ')
        

def makelist(x):
    theList = []
    for i in range(x):
        ranNum = random.randint(1,100)
        theList.append(ranNum)
    return theList

main()



