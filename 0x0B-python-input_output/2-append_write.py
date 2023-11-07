#!/usr/bin/python3
"""
this define the append write function
"""


def append_write(filename, text=""):
    """
    Appends a string to the end of a UTF8 text file
    """
    with open(filename, mode='a', encoding='utf-8') as f:
        return f.write(text)
