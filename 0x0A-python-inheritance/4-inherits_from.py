#!/usr/bin/python3
""" this define the inherits_from function"""


def inherits_from(obj, a_class):
    """
    Check if an object is an instance of a class that inherited
    (directly or indirectly)
    from the specified class.

    Args:
        obj: The object to check.
        a_class: The class to compare with.

    Returns:
        True if obj is an instance of a class that inherited from
        a_class, otherwise False.
    """
    return issubclass(type(obj), a_class) and type(obj) is not a_class
