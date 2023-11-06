#!/usr/bin/python3
"""
This define the the function thats return
true if object is an instance or
if the object is an instance of a class that inherited from the specified class: otherwise false
"""


def is_kind_of_class(obj, a_class):
    """
    returns true if the object is an instance
            or is an instance of a class inherited from
            else
            return false
    Args:
        :obj
        :a_class
    """
    return isinstance(obj, a_class)
