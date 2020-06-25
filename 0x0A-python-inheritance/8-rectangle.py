#!/usr/bin/python3
'''Create a class named BaseGeometry'''


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    '''A rectangle class that inherits from BaseGeometry class'''

    def __init__(self, width, height):
        self.__width = self.integer_validator("width", width)
        self.__height = self.integer_validator("height", height)
