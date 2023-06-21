#!/usr/bin/python3
"""MyList Class that inherits from List
"""



def append_write(filename="", text=""):
    """
    Append a string to the end of a text file (UTF8) and return the number 

    Args:
        filename (str): The name of the file to append (default: empty string).
        text (str): The string to append to the file.

    Returns:
        int: The number of characters added to the file.
    """
    with open(filename, mode='a', encoding='utf-8') as file:
        return file.write(text)
