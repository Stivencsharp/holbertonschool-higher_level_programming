#!/usr/bin/python3
first_digit = "0"
for num in range(0, 99):
    if num > 9:
        first_digit = ""
    print(first_digit + "{:d}, ".format(num), end="")
print("{}".format(99))
