#!/usr/bin/python3
def text_indentation(text):
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    separators = [".", "?", ":"]
    result = ""
    new_line = True

    for char in text:
        if new_line and char == " ":
            continue
        result += char
        if char in separators:
            result += "\n\n"
            new_line = True
        else:
            new_line = False

    print(result.strip(), end="")
