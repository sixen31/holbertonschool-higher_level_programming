#!/usr/bin/python3


"""
This is the "Rectangle" module.
This module provides a simple rectangle class.
"""


class Rectangle:
    """
    Class that defines a rectangle
    """

    def __init__(self, width=0, height=0):
        """
        Method that initializes the instance
        Args:
            width: width of the rectangle
            height: height of the rectangle
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        Getter method for width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Setter method for width
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """
        Getter method for height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Setter method for height
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """
        Method that calculates the area of the rectangle
        """
        return self.__height * self.__width

    def perimeter(self):
        """
        Method that calculates the perimeter of the rectangle
        """
        if self.width == 0 or self.height == 0:
            return 0
        return (self.__height + self.__width) * 2

    def __str__(self):
        """
        Method that returns the string representation of the rectangle
        """
        rectangle = ""

        if self.width == 0 or self.height == 0:
            return rectangle

        for i in range(self.height):
            rectangle += "#" * self.width + "\n"

        return rectangle[:-1]
