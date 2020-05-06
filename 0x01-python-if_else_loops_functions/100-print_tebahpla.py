#!/usr/bin/python3
num = 26
while num > 0:
    if num % 2 != 0:
        char = num + 64
    else:
        char = num + 96
    print("{:s}".format(chr(char)), end="")
    num -= 1
