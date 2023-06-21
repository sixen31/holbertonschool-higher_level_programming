#!/usr/bin/python3
"""MyList Class that inherits from List
"""


def write_file(filename="", text=""):
    """
    Write a string to a text file (UTF8) and return the number of characters

    Args:
        filename (str): The name of the file to write (default: empty string).
        text (str): The string to write to the file.

    Returns:
        int: The number of characters written to the file.
    """
    with open(filename, mode='w', encoding='utf-8') as file:
        return file.write(text)
