#!/usr/bin/python3
"""MyList Class that inherits from List
"""


def read_file(filename=""):
    """
    Read the content of a file and print it to stdout.

    Args:
        filename (str): The name of the file to read (default: empty string).

    Returns:
        None
    """
    with open(filename, encoding='utf-8') as file:
        print(file.read(), end='')
