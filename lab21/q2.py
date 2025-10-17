#!/usr/bin/pyhton3
# (2) Idea of inheritance- parent and child classes. Extend the Quadrilateral 
# class with two child classes - Square and Rectangle.In the constructor of 
# the child classes, call the parent’s constructor with a single side or 2 sides as 
# the case may be. Define functions getArea() in the child classes that return the
# area of the square or the rectangle.

class Quadrilateral:
    def __init__(self, a, b, c, d):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
    def square(self):
        return self.a == self.b == self.c == self.d
    def rectangle(self):
        return (self.a == self.c) and (self.b == self.d)

class Square(Quadrilateral):
    def __init__(self, side):
        Quadrilateral.__init__(self, side, side, side, side)
    def get_area(self):
        return self.a * self.a

class Rectangle(Quadrilateral):
    def __init__(self, length, breadth):
        Quadrilateral.__init__(self, length, breadth, length, breadth)
    def get_area(self):
        return self.a * self.b

a = int(input("Enter side 1: "))
b = int(input("Enter side 2: "))
c = int(input("Enter side 3: "))
d = int(input("Enter side 4: "))

quad = Quadrilateral(a, b, c, d)

if quad.square():
    sq = Square(a)
    print("It is a Square.")
    print("Area:", sq.get_area())
elif quad.rectangle():
    rect = Rectangle(a, b)
    print("It is a Rectangle.")
    print("Area:", rect.get_area())
else:
    print("The sides do not form a Square or Rectangle.")
