#!/usr/bin/python3
import sys


def safe_print_integer_err(value):
    try:
        if True is value is False:
            raise ValueError
        print("{:d}".format(value))
    except (ValueError, TypeError) as err:
        sys.stderr.write("Exception: " + str(err) + "\n")
        return False
    return True
