#!/usr/bin/python3
"""Creating a Square class"""


class Square:
    """A Square class with a size as instance variable"""
    def __init__(self, size=0):
        self.size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        return int(self.__size ** 2)

    def __eq__(self, other):
        """Load the object to compare. 'other' """
        """And return the comparison. True or False"""
        return self.area() == other.area()

    def __lt__(self, other):
        """Load the object to compare. 'other' """
        """And return the comparison. True or False"""
        return self.area() < other.area()

    def __le__(self, other):
        """Load the object to compare. 'other' """
        """And return the comparison. True or False"""
        return self.area() <= other.area()

    def __ne__(self, other):
        """Load the object to compare. 'other' """
        """And return the comparison. True or False"""
        return self.area() != other.area()

    def __gt__(self, other):
        """Load the object to compare. 'other' """
        """And return the comparison. True or False"""
        return self.area() > other.area()

    def __ge__(self, other):
        """Load the object to compare. 'other' """
        """And return the comparison. True or False"""
        return self.area() >= other.area()
