#!/usr/bin/py
class Quadrilateral:
    def __init__(self, side1, side2, side3, side4):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3
        self.side4 = side4

    def Square(self):
        return self.side1 == self.side2 == self.side3 == self.side4

    def Rectangle(self):
        return self.side1 == self.side3 and self.side2 == self.side4


# Taking input for each side individually
side1 = int(input("Enter side 1: "))
side2 = int(input("Enter side 2: "))
side3 = int(input("Enter side 3: "))
side4 = int(input("Enter side 4: "))

quad = Quadrilateral(side1, side2, side3, side4)

if quad.Square():
    print("The quadrilateral is a Square.")
elif quad.Rectangle():
    print("The quadrilateral is a Rectangle.")
else:
    print("The quadrilateral is neither a Square nor a Rectangle.")
