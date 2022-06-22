#!/usr/bin/python3
""" module 2-square"""


class Square:
    """Class Square that defines a square """


def __init__(self, size=0):
    try:
        if (size < 0):
            raise ValueError
            raise NameError('size must be >= 0')
        self.__size = size
    except type(size) != int:
        print("size must be an integer")
