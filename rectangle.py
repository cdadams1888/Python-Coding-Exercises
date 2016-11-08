# prompt the user to enter the length and width of a rectangle.
# create a new Rectangle instance with the dimensions entered by the user.
# to verify the above step, print both dimensions using their respective "getter" methods.
# test the area() method by printing the rectangle area accurate to two decimal places.
# test the perimeter() method by printing the rectangle perimeter accurate to two decimal places.
# change the length to 22.345 and change the width to 15.789.
# test the area() and perimeter() methods again. You should get the results shown in the sample output.

class Rectangle:
    def __init__(self, length, width):
        self.__length = length
        self.__width  = width

    def set_length(self, length):
        self.__length = length

    def set_width(self, width):
        self.__width = width

    def get_length(self):
        return self.__length

    def get_width(self):
        return self.__width

    def area(self, length, width):
        area = length * width
        print("Rectangle area is","{0:.2f}".format(round(area,2)))

    def perimeter(self, length, width):
        perimeter = (length + width) * 2
        print("Rectangle perimeter is","{0:.2f}".format(round(perimeter,2)))

def main():
    length = float(input("Enter the length of the rectangle: "))
    width  = float(input("Enter the width of the rectangle: "))
    rectangleObject = Rectangle(length, width)
    rectangleObject.set_length(length) # set the length
    rectangleObject.set_width(width) # set the width
    print(rectangleObject.get_length())
    print(rectangleObject.get_width())
    rectangleObject.area(length, width)
    rectangleObject.perimeter(length, width)
    # mutator / setter methods below
    rectangleObject.set_length(22.345)
    rectangleObject.set_width(15.789)
    print(rectangleObject.get_length())
    print(rectangleObject.get_width())
main()
