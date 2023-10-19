#!/usr/bin/python3
"""define python"""


def read_file(filename=""):
    """Reads a text file and prints its contents to stdout.

    Args:
        filename (str): The name of the file to be read. Defaults to "".

    Returns:
        None
    """
    with open(filename, encoding='utf-8') as file:
        print(file.read(), end='')
