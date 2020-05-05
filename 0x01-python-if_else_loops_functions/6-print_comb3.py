#!/usr/bin/python3
for first_digit in range(0, 8):
    second_digit = 1 + first_digit
    for second_digit in range(second_digit, 10):
        print("{}{}, ".format(first_digit, second_digit), end="")
print(89)
