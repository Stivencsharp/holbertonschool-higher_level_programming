#!/usr/bin/python3
def max_integer(my_list=[]):
    if not my_list:
        return None
    biggest_num = my_list[0]
    for num in my_list:
        if biggest_num < num:
            biggest_num = num
    return biggest_num
