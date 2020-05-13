#!/usr/bin/python3
import sys
arguments_len = len(sys.argv)
if arguments_len < 2:
    print("0 arguments.")
else:
    print("{:d} arguments:".format(arguments_len))
    for arg in range(1, arguments_len):
        print("{:d}: {:s}".format(arg, sys.argv[arg]))
