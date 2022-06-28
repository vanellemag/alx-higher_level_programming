#!/usr/bin/python3
""" 0-add_integer"""


def add_integer(a, b=98):
    """Function that adds 2 integers"""

    try:
        if (type(a) == int or type(a) == float):
            if (type(b) == int or type(b) == float):
                return int(a) + int(b)
        if type(a) != int or type(a) != float:
            raise TypeError("a must be an integer")
        if type(b) != int or type(b) != float:
            raise TypeError("b must be an  integer")
    except TypeError:
        raise
