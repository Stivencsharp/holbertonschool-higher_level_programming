#!/usr/bin/python3
'''Function with a class as argument
that return the result of the function dir()'''


def lookup(obj):
    '''Function to return the attributes and methods
    available in a class'''

    return dir([obj])
