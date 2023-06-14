#!/usr/bin/python3
"""
This module contains a function that adds 2 integers.

"""


def add_integer(a, b=98):
    """
    This function adds two integers.

    Args:
    a: integer or float.
    b: integer or float.

    Returns:
    The sum of two integers.

    Raises:
    TypeError: If a or b is not an int or a float.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
