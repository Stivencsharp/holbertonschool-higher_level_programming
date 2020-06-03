#!/usr/bin/python3
if __name__ == "__main__":
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


value = 89
has_been_print = safe_print_integer_err(value)
if not has_been_print:
    print("{} is not an integer".format(value))

value = -89
has_been_print = safe_print_integer_err(value)
if not has_been_print:
    print("{} is not an integer".format(value))

value = "Holberton"
has_been_print = safe_print_integer_err(value)
if not has_been_print:
    print("{} is not an integer".format(value))