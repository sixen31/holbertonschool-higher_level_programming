#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None

    max_score = None
    best_key = None
    for key in a_dictionary:
        value = a_dictionary[key]
        if max_score is None or value > max_score:
            max_score = value
            best_key = key

    return best_key
