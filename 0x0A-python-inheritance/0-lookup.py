#!/usr/bin/python3
'''Function with an object as argument
that return the result of the function dir()'''


def lookup(obj):
    '''Function to return the attributes and methods
    available in an object'''

    return dir(obj)


class MyClass1(object):
    pass
