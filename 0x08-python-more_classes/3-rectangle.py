#!/usr/bin/python3
"""Create a Rectangle Class"""


class Rectangle:
    """Rectangle Class with two attrbutes. Width and Height"""

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

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
        return self.height * self.width

    def perimeter(self):
        if self.height == 0 or 0 == self.width:
            return 0
        return (self.height + self.width) * 2

    def __str__(self):
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
