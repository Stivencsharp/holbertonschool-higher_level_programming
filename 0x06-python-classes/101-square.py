#!/usr/bin/python3
"""Creating a Square class"""


class Square:
    """A Square class with a size as instance variable"""

    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, position):
        err_message = ("position must be a tuple "
                       "of 2 positive integers")
        if len(position) != 2:
            raise TypeError(err_message)
        for item in position:
            if not isinstance(item, int):
                raise TypeError(err_message)
            if item < 0:
                raise ValueError(err_message)
        self.__position = position

    def area(self):
        return self.__size ** 2

    def __str__(self):
        self.my_print()
        return ''

    def my_print(self):
        if self.size == 0:
            print()
        else:
            print(self.position[1] * '\n', end='')
            for column in range(self.size):
                print("{}{}".format(self.position[0] * ' ',
                                    self.size * '#'), end='')
                print()


my_square = Square(5, (0, 0))
print(my_square)

print("--")

my_square = Square(5, (4, 1))
print(my_square)