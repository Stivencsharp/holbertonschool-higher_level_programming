#!/usr/bin/python3
'''Holberton task about instances of classes'''


def is_same_class(obj, a_class):
    '''Check if the object is instance of the class
    Return True if it is, if not, return False'''

    return type(obj) is a_class
