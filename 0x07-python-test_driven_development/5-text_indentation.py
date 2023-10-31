#!/usr/bin/python3

"""
This module contains a function that indents text.
"""

def text_indentation(text):
    """
    This function prints text with 2 new lines after each ".", "?", or ":"

    Args:
        text (str): The string to be formatted

    Raises:
        TypeError: If text is not a string
    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    cnt = 0
    while cnt < len(text) and text[cnt] == " ":
        cnt += 1

    while cnt < len(text):
        print(text[cnt], end="")
        if text[cnt] == "\n" or text[cnt] in ".?:":
            if text[cnt] in ".?:":
                print("\n")
            cnt += 1
            while cnt < len(text) and text[cnt] == " ":
                cnt += 1
            continue
        cnt += 1
