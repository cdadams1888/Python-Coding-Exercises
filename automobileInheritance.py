class Automobile:
    def __init__(self, make, model, mileage, price):
        self.__make    = make
        self.__model   = model
        self.__mileage = mileage
        self.__price   = price

    def setMake(self, make):
        self.__make = make

    def setModel(self, model):
        self.__model = model

    def setMileage(self, mileage):
        self.__mileage

    def setPrice(self, price):
        self.__price

    def getMake(self):
        return self.__make

    def getModel(self):
        return self.__model

    def getMileage(self):
        return self.__mileage

    def getPrice(self):
        return self.__price


# Car class is subclass of Automobile
class Car(Automobile):
    def __init__(self, make, model, mileage, price, doors):
        Automobile.__init__(self, make, model, mileage, price)
        self.__doors = doors # initialize the doors attribute

    def setDoors(self, doors):
        self.__doors = doors

    def getDoors(self):
        return self.__doors


def main():
    usedCar = Car("Toyota", 2007, 10000, 5000, 4)
    print('Make:', usedCar.getMake())
    print('Model:', usedCar.getModel())
    print('Mileage:', usedCar.getMileage())
    print('Price:', usedCar.getPrice())
    print('Doors:', usedCar.getDoors())
main()
