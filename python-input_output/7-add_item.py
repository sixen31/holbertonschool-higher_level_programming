#!/usr/bin/python3
"""Script that adds all arguments to a Python list and saves them to a file."""

import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

filename = "add_item.json"
try:
    # Try to load existing items from file
    items = load_from_json_file(filename)
except FileNotFoundError:
    # If file doesn't exist, create an empty list
    items = []

# Add the arguments to the list
items.extend(sys.argv[1:])

# Save the updated list to the file
save_to_json_file(items, filename)
