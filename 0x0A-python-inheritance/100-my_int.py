#!/usr/bin/python3
'''Create a class that inherit from int'''


class MyInt(int):
    '''A class that invert the  != and == comparators'''

    def __init__(self, value):
        self.__value = value

    def __eq__(self, other):
        return self.__value != other

    def __ne__(self, other):
        return self.__value == other
