#!/usr/bin/python3
"""This script is intended to be executed using Python 3."""


class MyList(list):
    """"A class that inherits from list."""
    def print_sorted(self):
        print(sorted(self))
