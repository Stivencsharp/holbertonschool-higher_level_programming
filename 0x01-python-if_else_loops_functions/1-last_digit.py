#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    last_digit = number % -10
else:
    last_digit = number % 10
if last_digit > 5:
    is_than = "and is greater than 5"
elif last_digit is 0:
    is_than = "and is 0"
else:
    is_than = "and is less than 6 and no 0"
print("Last digit of " + str(number) + " is " + str(last_digit), is_than)
