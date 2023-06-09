#!/usr/bin/python3
"""
This is the "Square" module.
This module provides a simple Square class with an initialized size.
"""


class Square:
    """A class that defines a Square by size"""
    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """This is a public instance method"""
        return self.__size * self.__size
