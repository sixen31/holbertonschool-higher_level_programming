#!/usr/bin/python3
"""A script that adds all arguments to a Python list,
and then saves them to a file
"""


import sys
from os.path import exists
from 5-save_to_json_file import save_to_json_file
from 6-load_from_json_file import load_from_json_file

filename = "add_item.json"

if exists(filename):
    try:
        json_list = load_from_json_file(filename)
    except Exception:
        json_list = []
else:
    json_list = []

for item in sys.argv[1:]:
    json_list.append(item)

save_to_json_file(json_list, filename)
