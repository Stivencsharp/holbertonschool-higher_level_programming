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
        return self.__size ** 2

    def my_print(self):
        if self.size == 0:
            print()
        else:
            for column in range(self.size):
                for row in range(self.size):
                    print("#", end='')
                print()