#!/usr/bin/python3
class Square:
    def __init__(self, size=0):
        """
        Initializer method that creates a new Square object with a given size.

        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """
        Calculates and returns the area of the square.

        """
        return self.__size ** 2
