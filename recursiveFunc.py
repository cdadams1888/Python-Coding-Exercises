# Design a recursive function that prints each character of a string on its own line.
# The function should take only one argument, the string to be processed.
# The string to be processed should be entered by the user.
a = 0
theArg = str(input("Enter your string: "))
def recursiveFunc(x):
    global a
    while len(x) > a:
        print(x[a])
        a += 1
        recursiveFunc(theArg)

recursiveFunc(theArg)
