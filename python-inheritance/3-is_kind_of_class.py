#!/usr/bin/python3
"""Same class or inherit from"""


def is_kind_of_class(obj, a_class):
    """Return True if obj is an instance"""
    return type(obj) is a_class or isinstance(obj, a_class)
