#!/usr/bin/python3

'''Return if a obj inherits from a class'''


def inherits_from(obj, a_class):
    '''Return True is a object inherits from a class. Otherwise, return False.'''

    return a_class is not type(obj) and issubclass(type(obj), a_class)
