#!/usr/bin/python3
def safe_print_integer(value):
    try:
        if True is value is False:
            raise ValueError
        print("{:d}".format(value))
    except (ValueError, TypeError):
        return False
    return True
