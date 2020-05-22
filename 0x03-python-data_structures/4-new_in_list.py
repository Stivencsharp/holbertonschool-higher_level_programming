#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    new_list = my_list.copy()
    if 0 > idx or idx > len(my_list) - 1:
        return new_list
    my_list.pop(idx)
    my_list.insert(idx, element)
    return new_list
