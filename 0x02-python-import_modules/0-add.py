#!/usr/bin/python3
_sum = __import__('add_0').add
a, b = 1, 2
print("{:d} + {:d} = {:d}".format(a, b, _sum(1, 2)))
