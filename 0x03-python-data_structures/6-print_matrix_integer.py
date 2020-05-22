#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for _list in matrix:
        space = ''
        for item in _list:
            print("{}{:d}".format(space, item), end='')
            space = ' '
        print()
