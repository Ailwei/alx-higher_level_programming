#!/usr/bin/python3
"""
define the add_attribute function
"""
def add_attribute(obj, attr_name, attr_value):
    """
    Adds a new attribute to an object if possible, raises TypeError if not possible.

    Args:
        obj: The object to which the attribute should be added.
        attr_name: The name of the attribute.
        attr_value: The value of the attribute.

    Raises:
        TypeError: If the object can't have new attributes.
    """
    if hasattr(obj, '__dict__'):
        # The object can have new attributes
        setattr(obj, attr_name, attr_value)
    else:
        # The object can't have new attributes
        raise TypeError("can't add new attribute")
