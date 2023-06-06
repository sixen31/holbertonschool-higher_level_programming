#!/usr/python3
def replace_in_list(my_list, idx, element):
    while idx in my_list:
        my_list.insert(my_list.index(idx), element)
        my_list.pop(my_list.index(idx))
    return my_list
