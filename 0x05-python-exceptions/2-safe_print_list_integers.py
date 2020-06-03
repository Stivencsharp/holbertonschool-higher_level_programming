#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    num_prints = 0
    for value in range(x):
        try:
            if True is my_list[value] is False:
                raise ValueError
            print("{:d}".format(my_list[value]), end='')
            num_prints += 1
        except (ValueError, TypeError):
            continue
    print()
    return num_prints
