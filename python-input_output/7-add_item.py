#!/usr/bin/python3
"""Add arguments to a Python list and save to a JSON file."""

import sys
import json

def save_to_json_file(my_obj, filename):
    """Writes an object to a text file using a JSON representation."""
    with open(filename, mode='w', encoding='utf-8') as file:
        json.dump(my_obj, file)

def load_from_json_file(filename):
    """Creates an object from a JSON file."""
    try:
        with open(filename, mode='r', encoding='utf-8') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

args = sys.argv[1:]
