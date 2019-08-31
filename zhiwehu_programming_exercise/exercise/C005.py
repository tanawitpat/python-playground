"""
Define a class named Shape and its subclass Square. The Square class has an init function which takes a length as argument. Both classes have a area function which can print the area of the shape where Shape's area is 0 by default.

Hints:

To override a method in super class, we can define a method with the same name in the super class.
"""

class Shape():
    def __init__(self):
        self.area = 0

class Square(Shape):
    def __init__(self, length):
        self.area = length ** 2

square1 = Square(length=5)
print(square1.area) # 25