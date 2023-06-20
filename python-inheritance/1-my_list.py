#!/usr/bin/python3
"""MyList Class that inherits from List
"""


class MyList(list):
    """_summary_

    Args:
        list (_type_): _description_
    """
    def print_sorted(self):
        print(sorted(self))
