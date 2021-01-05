#!/usr/bin/python3


def safe_function(fct, *args):
    try:
        a = fct(*args)
    except (ZeroDivisionError, IndexError) as error:
        print("Exception: " + str(error))
        return None
    return a
