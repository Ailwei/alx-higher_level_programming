#!/usr/bin/python3
def lookup(obj):
    """
    Return a list of available attributes and methods of an object (excluding special methods).

    Args:
        obj (object): The object for which to retrieve attributes and methods.

    Returns:
        list: A list of attribute and method names.

    This function uses the `dir()` function to obtain a list of all attributes and methods of the object.
    It filters out special methods (those starting with double underscores) and returns the remaining names.
    """
    # Get the list of attributes and methods using dir()
    attributes_and_methods = dir(obj)
    
    # Filter out attributes and methods that start with '__' (special methods)
    filtered_attributes_and_methods = [item for item in attributes_and_methods if not item.startswith('__')]
    
    return filtered_attributes_and_methods
