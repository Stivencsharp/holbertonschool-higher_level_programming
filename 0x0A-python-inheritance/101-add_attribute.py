#!/usr/bin/python3
def add_attribute(a_class, name, value):
    if not (setattr(a_class, name, value)):
        raise TypeError("can't add new attribute")
