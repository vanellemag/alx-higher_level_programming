#!/usr/bin/python3
""""4-square"""


class Square:
    """ Class Square that defines a square"""

    def size(self):
        """ Property to retrieve it"""
        self.__size

    def __init__(self, size=0):
        """ instantion with optional"""
        self.size = size

    def size(self, value):
        """ property setter to set it"""
        try:
            if type(size) == int:
                self.__size = size
            else:
                raise TypeError('size must be an integer')
            if size < 0:
                raise ValueError('size must be >= 0')
        except TypeError:
            raise

    def area(self):
        """ method that returns the current square area"""
        return self.__size * self.__size
