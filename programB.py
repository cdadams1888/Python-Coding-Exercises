'''Use the text file named scores.txt (supplied).
It contains a number of integer test scores, one per line.
Your program should use a main function and another function named
showscores as follows:
in main, create an empty list.
open the file named scores.txt.
use a while loop that can detect the end of file to read the scores,
and add them to the list.
close the file.
call the showscores function with the list of scores as sole argument.
inside the showscores function:
process the list of scores. NOTE: your instructor will use a
modified version of
scores.txt with different scores and a different number of scores.
Your code should be capable of handling this.
print out the average score accurate to two decimal places.'''

def showscores(theList):
    print(theList)

def main():
    theList = []
    theFile = open('scores.txt', 'r')
    readLines = theFile.readline().rstrip('\n')
    while(readLines != ''):
        theList.append(readLines)
        readLines = theFile.readline().rstrip('\n')
    theFile.close()
    showscores(theList)
main()
