#!/usr/bin/pyhton3
"""Class definition"""


class Rectangle:
    """This class defines a square"""
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    def get_width(self):
        return self.__width

    def set_width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    def get_height(self):
        return self.__height

    def set_height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    width = property(get_width, set_width)
    height = property(get_height, set_height)
