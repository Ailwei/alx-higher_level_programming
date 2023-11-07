"""Writes a string-to-JSON function."""
import json


def to_json_string(my_obj):
    """
    Return the JSON representation of an object as a string.

    :param my_obj: The object to be converted to JSON.
    :return: A JSON string representation of the object.
    :rtype: str
    """
    return json.dumps(my_obj)
