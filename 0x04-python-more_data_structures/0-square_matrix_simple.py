#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = [[item**2 for item in sublist] for sublist in matrix]
    return new_matrix
