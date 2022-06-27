#!/usr/bin/python3
"""3-rectangle"""


class Rectangle:
    """class that defines a rectangle"""

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        try:
            if type(value) == int:
                raise TypeError("width must be an integer")
            elif value < 0:
                raise ValueError("width must be >= 0")
            else:
                self._width = value
        except TypeError:
            raise

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        try:
            if type(value) == int:
                raise TypeError("height must be an integer")
            elif value < 0:
                raise ValueError("height must be >= 0")
            else:
                self._height = value
        except TypeError:
            raise

    def __init__(self, width=0, height=0):
        self._width = width
        self._height = height

    def area(self):
        return self._width * self._height

    def perimeter(self):
        if self._width == 0 or self._height == 0:
            return 0
        else:
            return 2 * (self._width + self._height)

    def printe(self, width, height):
        if self._width == 0 or self._height == 0:
            str('')
        else:
            for i in range(self._width):
                for j in range(self._height):
                    str('#')
