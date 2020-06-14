#!/usr/bin/python3
'''Create a class MyList that inherits from list'''


class MyList(list):
    '''Class MyList that inherits from list'''

    def print_sorted(self):
        list_copy = self.copy()
        list_copy.sort()
        print(list_copy)

    def __str__(self):
        list_copy = self.copy()
        return "{}".format(list_copy)
