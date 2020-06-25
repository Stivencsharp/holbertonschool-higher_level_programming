#!/usr/bin/python3
'''Create a class named BaseGeometry'''


class BaseGeometry:
    '''A class BaseGeometry with a instance method area()'''

    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if type(value) is not int:
            raise TypeError("{:s} must be an integer".format(name))
        elif value < 1:
            raise ValueError("{:s} must be greater than 0".format(name))
        return value


class Rectangle(BaseGeometry):
    '''A rectangle class that inherits from BaseGeometry class'''

    def __init__(self, width, height):
        self.__width = self.integer_validator("width", width)
        self.__height = self.integer_validator("height", height)
