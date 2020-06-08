#!/usr/bin/python3
"""Create a Rectangle Class"""


class Rectangle:
    """Rectangle Class with two attrbutes. Width and Height"""
    """Class variables: type int number_of_instances"""
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    def __del__(self):
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width):
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        self.__width = width

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__height = height

    def area(self):
        """The area based on the height by the width"""
        return self.height * self.width

    def perimeter(self):
        """The perimeter based on the height and width by 2"""
        if self.height == 0 or 0 == self.width:
            return 0
        return (self.height + self.width) * 2

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if type(rect_1) is not Rectangle:
            raise TypeError("rect_1 must be an instance of Rectangle")
        if type(rect_2) is not Rectangle:
            raise TypeError("rect_2 must be an instance of Rectangle")
        r1 = rect_1.height * rect_1.width
        r2 = rect_2.height * rect_2.width
        if r1 == r2 or r1 > r2:
            return rect_1
        return rect_2

    @staticmethod
    def square(cls, size=0):
        new_instance = Rectangle(size, size)
        return new_instance

    def __str__(self):
        """Print the Rectangule based on the height and the width"""
        if self.height == 0 or 0 == self.width:
            return ""
        rect_str = ""
        for column in range(self.height):
            if column == self.height - 1:
                rect_str += "{}".format(self.width * str(self.print_symbol))
            else:
                rect_str += "{}\n".format(self.width * str(self.print_symbol))
        return rect_str

    def __repr__(self):
        """Return the string representation of rectangle"""
        return "Rectangle({}, {})".format(self.width, self.height)


Rectangle = __import__('9-rectangle').Rectangle

my_square = Rectangle.square(5)
print("Area: {} - Perimeter: {}".format(my_square.area(), my_square.perimeter()))
print(my_square)
