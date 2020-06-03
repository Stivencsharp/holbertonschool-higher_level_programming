#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    div_list = []
    for divs in range(list_length):
        try:
            div_list.append(my_list_1[divs] / my_list_2[divs])
        except ZeroDivisionError:
            print("division by 0")
            div_list.append(0)
        except TypeError:
            print("wrong type")
            div_list.append(0)
        except IndexError:
            print("out of range")
            div_list.append(0)
    return div_list
