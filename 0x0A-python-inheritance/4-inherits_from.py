#!/usr/bin/python3
def inherits_from(obj, a_class):
    return a_class is not type(obj) and issubclass(type(obj), a_class)
