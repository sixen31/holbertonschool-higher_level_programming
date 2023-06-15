#!/usr/bin/python3
"""Class definition"""


class Square:
    """This class defines a square."""

    def __init__(self, size=0):
        self.size = size

    @property
    def size(self):
        """Getter method to retrieve size."""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter method to set size."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """Returns the current square area."""
        return self.__size ** 2
