#!/usr/bin/python3
'''Create a class named Square'''


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    '''A rectangle class that inherits from BaseGeometry class'''

    def __init__(self, size):
        self.__size = self.integer_validator("size", size)

    def __str__(self):
        return "[Square] {0:d}/{0:d}".format(self.__size)

    def area(self):
        return self.__size ** 2
