#!/usr/bin/python3
def no_c(my_string):
    new_string = ""
    for letter in my_string:
        if 'c' != letter != 'C':
            new_string += letter
    return new_string


print(no_c("Cosas cagadas"))
