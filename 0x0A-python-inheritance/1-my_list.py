#!/usr/bin/python3
'''Create a class MyList that inherits from list'''


class MyList(list):
    '''Class MyList that inherits from list'''

    def __init__(self):
        self._list = []

    def print_sorted(self):
        print(sorted(self._list))

    def append(self, value):
        self._list.append(value)

    def __str__(self):
        print(self._list, end='')
        return ''


my_list = MyList()
my_list.print_sorted()
