#!/usr/bin/python3
"""MyList Class that inherits from List
"""


class MyList(list):
    """summary

    Args:
        list (type): description
    """
    def print_sorted(self):
        print(sorted(self))
