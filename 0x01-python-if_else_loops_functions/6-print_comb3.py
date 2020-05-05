#!/usr/bin/python3
numbers = "{}{}, "
for first_digit in range(0, 9):
    second_digit = 1 + first_digit
    for second_digit in range(second_digit, 10):
        if first_digit is 8 and second_digit is 9:
            numbers = "{}{}"
        print(numbers.format(first_digit, second_digit), end="")

