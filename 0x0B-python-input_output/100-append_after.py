#!/usr/bin/python3
"""
append function definition
"""


def append_after(filename="", search_string="", new_string=""):
    """
    Inserts text after each line containing a given string in a file.

    Args:
        filename (str): The name of the file.
        search_string (str): The string to search for within the file.
        new_string (str): The string to insert.
    """
    text = ""
    with open(filename) as faila:
        for line in faila:
            text += line
            if search_string in line:
                text += new_string
    with open(filename, "w") as W:
        W.write(text)
