#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    len_a, len_b = len(tuple_a),  len(tuple_b)
    sum1 = (0 if len_a < 1 else tuple_a[0]) + (0 if len_b < 1 else tuple_b[0])
    sum2 = (0 if len_a < 2 else tuple_a[1]) + (0 if len_b < 2 else tuple_b[1])
    new_tuple = (sum1, sum2)
    return new_tuple
