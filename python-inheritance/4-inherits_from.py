#!/usr/bin/python3
"""MyList Class that inherits from List
"""


def inherits_from(obj, a_class):
    """Return True if obj is an instance of a class that inherite"""
    return isinstance(obj, a_class) and type(obj) is not a_class
