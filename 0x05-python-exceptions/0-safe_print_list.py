#!/usr/bin/bash
def safe_print_list(my_list=[], x=0):
    items_printed = 0
    for idx in range(x):
        try:
            print(my_list[idx], end='')
        except IndexError:
            break
        items_printed += 1
    print()
    return items_printed
