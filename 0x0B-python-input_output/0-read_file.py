#!/usr/bin/python3
"""
this define the read_file function
"""


def read_file(filename=""):
      """
    Read and print the content of a text file in UTF-8 encoding.

    :param filename: The path to the text file to be read.
    :type filename: str
    """
    try:
        with open(filename,mode='r',encoding='utf-8') as file:
            for line in file:
                print(line, end="")
    except FileNotFoundError:
        pass
