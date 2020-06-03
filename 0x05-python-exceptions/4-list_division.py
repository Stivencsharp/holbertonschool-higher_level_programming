#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    div_list = []
    for divs in range(list_length):
        current_result = 0
        try:
            current_result = my_list_1[divs] / my_list_2[divs]
        except ZeroDivisionError:
            print("division by 0")
        except TypeError:
            print("wrong type")
        except IndexError:
            print("out of range")
        finally:
            div_list.append(current_result)
    return div_list
