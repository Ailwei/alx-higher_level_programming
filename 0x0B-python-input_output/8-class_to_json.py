#!/usr/bin/python3
"""
h
"""


def class_to_json(obj):
    """
    Convert an object to a dictionary description for JSON serialization.

    :param obj: An instance of a class with serializable attributes.
    :return: A dictionary representation of the object.
    """
    if not isinstance(obj, object):
        raise ValueError("Input must be an instance of a class")

    # Get all attributes and their values using introspection
    attributes = {}
    for key, value in obj.__dict__.items():
        if isinstance(value, (list, dict, str, int, bool)):
            attributes[key] = value

    return attributes
