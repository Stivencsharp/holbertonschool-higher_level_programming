#!/usr/bin/python3
"""Creating a Square class"""


class Square:
    """A Square class with a size as instance variable"""
    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
