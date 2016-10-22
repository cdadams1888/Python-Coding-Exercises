# prompt the user to enter his/her full name (see sample output).
fullName = str(input("Enter your full name: "))
fullNameBackwards = ""

# display the number of characters in the full name.
print(len(fullName))
i = 0

# use a while loop to print the name backwards.
while i < len(fullName):
    i += 1
    backwards = fullName[len(fullName) - i]
    fullNameBackwards += backwards
print(fullNameBackwards)

# use slicing to make a new string in the format lastname, firstname. Print the new string.
newString = fullName.split()
print(newString[1], newString[0])

# use a loop and counter variables to determine the number of upper and lower case letters in
# the name. Print both totals.
lower = 0
upper = 0
for x in fullName:
    if(x.islower()):
        lower += len(x)
    if(x.isupper()):
        upper += len(x)
print("The number of lower case letters is", lower)
print("The number of upper case letters is", upper)

# assign "You have to be vewy, vewy twicky to twap a wascally wabbit" to another new string.
elmerSaying = "You have to be vewy, vewy twicky to twap a wascally wabbit"
# use a method to correct Elmer Fudd's bad spelling above. Print the corrected string.
print(elmerSaying.replace("w", "r"))
