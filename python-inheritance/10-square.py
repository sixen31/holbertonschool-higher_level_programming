#!/usr/bin/python3
"""A module with a class BaseGeometry"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Define Square class"""

    def __init__(self, size):
        self.__size = size
        super().__init__(size, size)
        self.integer_validator("size", size)

    def __str__(self):
        return "[Square] {}/{}".format(self.__size, self.__size)
