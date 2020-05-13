#!/usr/bin/python3
if __name__ == "__main__":
    _sum = __import__('add_0').add
a, b = 1, 2
print("{:d} + {:d} = {:d}".format(a, b, _sum(a, b)))
