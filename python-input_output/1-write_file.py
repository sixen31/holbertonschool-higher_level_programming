#!/usr/bin/python3
"""define python"""


def write_file(filename="", text=""):
    """Writes a string to a text file and returns the number of characters written.

    Args:
        filename (str): The name of the file to write to. Defaults to "".
        text (str): The string to be written to the file. Defaults to "".

    Returns:
        int: The number of characters written.
    """
    with open(filename, mode='w', encoding='utf-8') as file:
        return file.write(text)
