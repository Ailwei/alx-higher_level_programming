#!/usr/bin/python3

"""A module that contain square class"""


class Square:
    """Defines a 2D square with four equal sides and right angles.

Args:
    size (int): The size parameter that initializes
    the private instance attribute __size.

Attributes:
    __size (int): A private integer instance attribute.

Raises:
    TypeError: If __size attribute is not of integer type.
    ValueError: If __size attribute is less than zero.
"""

    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an Integer")
        elif size < 0:
            raise VlaueError("size must >= 0")
        self.__size = size

    def area(self):
        return self.__size ** 2
