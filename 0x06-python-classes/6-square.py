#!/usr/bin/python3
""""6-square"""


class Square:
    """Class that defines a square"""
    def size(self):
        """Property to retreive instance attribute"""
        self.__size

    def size(self, value):
        """property setter"""
        try:
            if type(value) == int:
                self.__size = value
            else:
                raise TypeError('size must be an integer')
            if self.__size < 0:
                raise ValueError('size must be >= 0')
        except TypeError:
            raise

    def position(self):
        """property position to retrieve instance attribute"""
        self.__position = ()

    def position(self, value):
        """property setter to set instance attribute"""
        try:
            self.__position = value
        except TypeError:
            raise TypeError('position must be a tuple of 2 positive integers')

    def __init__(self, size=0, position=(0, 0)):
        """Instantiation whit optional size and position"""
        self.__size = size
        self.__position = position

    def area(self):
        """instance method that returns the current square"""
        return self.__size * self.__size

    def my_print(self):
        """Instance method that prints in stdout the square with #"""
        if self.__size == 0:
            print()
            if self.__size > 0:
                if position[1] > 0:
                    for i in range(self.__size):
                        for j in range(self.__size):
                            print("#")
                        print()
                else:
                    for i in range(self.__size):
                        print("{}{}".format('_' * position[0], '#'), end="")
                        for j in range(self.__size - 1):
                            print("#")
                        print()
