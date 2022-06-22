#!/usr/bin/python3
"""4-square"""


class Square:
    """class that defines a square """

    def size(self):
        """property to retrieve it"""
        self.__size

    def size(self, value):
        """property setter to set it"""

        try:
            if type(value) == int:
                self.__size = value
            else:
                raise TypeError('size must be an integer')
            if self.__size < 0:
                raise ValueError('size must be >= 0')
        except TypeError:
            raise

    def __init__(self, size=0):
        """ instatntiation with size"""

        self.__size = size

    def area(self):
        """instance method that returns the currents square area"""

        return self.__size * self.__size

    def my_print(self):
        """Instane method that prints in stdout the square
        with the character #"""

        if self.__size == 0:
            print()
        if self.__size > 0:
            for i in range(self.__size):
                for j in range(self.__size):
                    print("#", end="")
                print()
