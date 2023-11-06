#!/usr/bin/python3
"""
deiine the fucntion that returns true or false
"""


def is_same_class(obj, a_class):
    """
    return true if object is the same as instance of the specified class
    or else return false
    """
    return type(obj) == a_class
