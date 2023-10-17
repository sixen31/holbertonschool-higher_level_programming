#!/usr/bin/python3
"""A module with a class BaseGeometry"""


class BaseGeometry:
    """A class with a no implemented method"""
    def area(self):
        """define area"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """define validator"""

        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        elif value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
