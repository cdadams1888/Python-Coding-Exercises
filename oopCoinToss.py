import random

class Coin:
    def __init__(self):  # __init__ method is an intializer method.
        self.sideup = "Heads" # self statement is kind of like the "this" keyword in JS.

    def toss(self):
        if random.randint(0,1) == 0:
            self.sideup = "Heads"
        else:
            self.sideup = "Tails"

    def get_sideup(self):
        return self.sideup

def main():
    my_coin = Coin() # Creates an object from the coin class.
    print('This side is up:', my_coin.get_sideup()) # Display the data of the coin facing up.

    # toss the coin
    print("I am tossing the coin...")
    my_coin.toss()

    # display the side of the coin that is facing up.
    print("This side is up: ", my_coin.get_sideup())

main()
