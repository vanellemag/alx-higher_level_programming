#!/usr/bin/python3
"""3-square"""


class Square:
    """Class Square that defines a square """

    def __init__(self, size=0):
        """Instantiation with optional"""
        try:
            if type(size) == int:
                self.__size = size
            else:
                raise TypeError("size must be an integer")
            if size < 0:
                raise ValueError("size must be >= 0")
        except ValueError:
            raise

    def area(self):
        """ Method that returns the current square area """
        return self.__size * self.__size
