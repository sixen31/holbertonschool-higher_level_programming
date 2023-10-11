#!/usr/bin/python3


def add_integer(a, b=98):
    """
    Adds two integers.

    :param a: The first integer.
    :param b: The second integer (default is 98).
    :return: The addition of a and b as an integer.
    """
    if type(a) not in (int, float):
        raise TypeError("a must be an integer")
    if type(b) not in (int, float):
        raise TypeError("b must be an integer")

    a = int(a)
    b = int(b)

    return a + b
