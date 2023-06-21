#!/usr/bin/python3
"""MyList Class that inherits from List
"""


import json


def save_to_json_file(my_obj, filename):
    """
    Save an object to a JSON file.

    Args:
        my_obj (object): Object to be saved.
        filename (str): Name of the file.

    Returns:
        None
    """
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(my_obj, file)
