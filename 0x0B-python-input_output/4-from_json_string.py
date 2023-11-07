#!/usr/bin/python3
"""
Writes a JSON-to-object function.
"""
import json


def from_json_string(my_str):
    """
    Parse a JSON string and return the corresponding Python data structure.

    :param my_str: The JSON string to be parsed.
    :type my_str: str
    :return: The Python data structure represented by the JSON string.
    """
    return json.loads(my_str)
