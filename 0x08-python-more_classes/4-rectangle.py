#!/usr/bin/python3
""" Create a Rectangle Class """


class Rectangle:
    """ Rectangle Class with two attrbutes. Width and Height """

    def __init__(self, width=0, height=0):

        """The init function with the width and height as arguments"""

        self.width = width
        self.height = height

    @property
    def width(self):

        """The getter function of the width attribute"""

        return self.__width

    @width.setter
    def width(self, width):

        """The setter function of the width attribute"""

        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        self.__width = width

    @property
    def height(self):

        """The getter function of the height attribute"""

        return self.__height

    @height.setter
    def height(self, height):

        """The setter function of the height attribute"""

        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__height = height

    def area(self):

        """The getter and setter function of the area attribute"""

        return self.height * self.width

    def perimeter(self):

        """The getter and setter function of the perimeter attribute"""

        if self.height == 0 or 0 == self.width:
            return 0
        return (self.height + self.width) * 2

    def __str__(self):

        """The str function to return a string with the rectangle in '#' based
        on the height and width"""

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

        """The repr function to return a string representation of the
        rectngle to recreate a new instance later"""

        return "Rectangle({}, {})".format(self.width, self.height)
