#!/usr/bin/python3
def uppercase(str):
    new_str = ""
    for letter in str:
        if 96 < ord(letter) < 123:
            new_str += chr(ord(letter) - 32)
        else:
            new_str += letter
    print("{:s}".format(new_str))
