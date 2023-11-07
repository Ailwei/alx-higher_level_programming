#!/usr/bin/python3
"""
write an object to file
"""
import json


def save_to_json_file(my_obj, filename):
    """
    Write an object to a text file using a JSON representation.

    :param my_obj: The object to be saved to the file.
    :param filename: The name of the file to write the JSON representation to.
    """
    with open(filename, mode='w', encoding='utf-8') as f:
        json.dump(my_obj, f, ensure_ascii=False)
