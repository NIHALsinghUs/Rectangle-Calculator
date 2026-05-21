# Creating a class named Rectangle
class Rectangle:

    # __init__ is a constructor
    # It runs automatically when an object is created
    def __init__(self , length , width):

        # self.length stores the length value inside the object
        self.length = length

        # self.width stores the width value inside the object
        self.width = width

    # Method to calculate area of rectangle
    def area_of_rectangle(self):

        # Formula: length × width
        return self.length * self.width

    # Method to calculate perimeter of rectangle
    def perimeter_of_rectangle(self):

        # Formula: 2(length + width)
        return 2 * ( self.length + self.width)


# Creating object of Rectangle class
# User enters length and width using input()
# int() converts string input into integer
rec = Rectangle(
    length = int(input("Enter the length : ")),
    width = int(input("Enter the width : "))
)


# f-string is used to print values inside {}
# rec.length accesses length from the object
# rec.width accesses width from the object
print(f"Length : {rec.length}, Width : {rec.width}")


# Calling area_of_rectangle() method
# It returns area of rectangle
print("Area of rectangle :",rec.area_of_rectangle())


# Calling perimeter_of_rectangle() method
# It returns perimeter of rectangle
print("Perimeter of rectangle :",rec.perimeter_of_rectangle())