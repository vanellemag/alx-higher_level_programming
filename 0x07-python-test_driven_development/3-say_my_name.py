#!/usr/bin/python3
"""
3-say_my_name modulle
write a function that prints name
firts name and last name
"""


def say_my_name(first_name, last_name=""):
    """
    function that prints first and last name
    """

    try:
        if type(first_name) == str:
            if type(last_name) == str:
                print("My name is {} {}".format(first_name, last_name))
            else:
                raise TypeError("last_name must be a string")
        else:
            raise TypeError("first_name must be a string")

    except TypeError:
        raise
