#!/usr/bin/python3

def add_integer(a, b=98):
    """
    Adds two integers.

    Args:
    a (int or float): The first integer or float.
    b (int or float, optional): The second integer or float. Defaults to 98.

    Returns:
    int: The addition of a and b.

    Raises:
    TypeError: If a or b is not an integer or float.
    """
    if not (isinstance(a, int) or isinstance(a, float)):
        raise TypeError("a must be an integer or b must be an integer")
    if not (isinstance(b, int) or isinstance(b, float)):
        raise TypeError("a must be an integer or b must be an integer")

    a = int(a)
    b = int(b)

    return a + b
