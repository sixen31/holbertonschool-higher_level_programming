#!/usr/bin/python3
"""define python"""


def inherits_from(obj, a_class):
    """define class"""
    return issubclass(type(obj), a_class) and type(obj) is not a_class
