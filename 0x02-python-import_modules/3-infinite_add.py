#!/usr/bin/python3
if __name__ == "__main__":
    import sys
_sum = 0
arg_len = len(sys.argv)
if arg_len > 1:
    for arg in range(1, arg_len):
        _sum += int(sys.argv[arg])
print("{:d}".format(_sum))
