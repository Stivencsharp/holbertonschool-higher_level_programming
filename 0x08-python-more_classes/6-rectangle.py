#!/usr/bin/python3
"""Create a Rectangle Class"""


class Rectangle:
    """Rectangle Class with two attrbutes. Width and Height"""
    """Class variables: type int number_of_instances"""
    number_of_instances = 0

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

    def __str__(self):
        """Print the Rectangule based on the height and the width"""
        if self.height == 0 or 0 == self.width:
            return ""
        rect_str = ""
        _rectangle = []
        for column in range(self.height):
            if column == self.height - 1:
                _rectangle.append(self.width * '#')
            else:
                _rectangle.append(self.width * '#' + '\n')
            rect_str += _rectangle[column]
        return rect_str

    def __repr__(self):
        """Return the string representation of rectangle"""
        return f'Rectangle({self.width}, {self.height})'
