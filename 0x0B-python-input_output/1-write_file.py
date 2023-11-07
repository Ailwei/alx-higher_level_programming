#!/usr/bin/python3
"""
This define the write_function
"""


def write_file(filename="", text=""):
    """
    Write a string to a text file (UTF-8) and return the number of characters written.

    :param filename: The name of the file to write to.
    :type filename: str
    :param text: The text to be written to the file.
    :type text: str
    :return: The number of characters written to the file.
    :rtype: int
    """

    char_count = len(text)
    file = open(filename, mode='w', encoding='utf-8')
    
    file.write(text)
        
    file.close()
    return char_count
