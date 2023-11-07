#!/usr/bin/python3
"""
make a json file
"""


def load_from_json_file(filename):
    """
     Create a Python object from a JSON file.

    :param filename: The name of the JSON file to read.
    :return: The Python object created from the JSON file content.
    """
    with open(filename, mode='w', encoding='utf-8') as f:
        return json.load(f)
