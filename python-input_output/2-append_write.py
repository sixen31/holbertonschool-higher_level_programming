#!/usr/bin/python3
"""Define Python3"""


def append_write(filename="", text=""):
    """Appends a string to the end of a text file and returns the number of characters added.

    Args:
        filename (str): The name of the file to append to. Defaults to "".
        text (str): The string to be appended to the file. Defaults to "".

    Returns:
        int: The number of characters added.
    """
    with open(filename, mode='a', encoding='utf-8') as file:
        return file.write(text)
