#!/usr/bin/python3
'''Create a function to check instances'''


def is_kind_of_class(obj, a_class):
    '''Check and return True if an object is instance of, or if the
    object is an instance of a class that inherit from, otherwise,
    return False.'''

    return isinstance(obj, a_class)
