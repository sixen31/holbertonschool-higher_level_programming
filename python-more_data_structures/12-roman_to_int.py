#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or roman_string is None:
        return 0

    roman_dict = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    result = 0
    prev_char = ''

    for char in roman_string:
        if char not in roman_dict:
            return 0

        if prev_char and roman_dict[prev_char] < roman_dict[char]:
            result -= roman_dict[prev_char]
            result += roman_dict[char] - roman_dict[prev_char]
        else:
            result += roman_dict[char]

        prev_char = char

    return result
