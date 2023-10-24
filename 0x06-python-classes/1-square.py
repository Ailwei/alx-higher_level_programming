#!/usr/bin/python3
"""this contains square class"""


class Square:
    """"a class square that defines a square with private instance attracribute
    args:
    value (int): a value that initilises ''_size'' attributr
    attributes:
    _size (int):  a private instance attribute
                       The size of a square is crucial for a square,
                       many things depend of it (area computation, etc.),
                       so i, as class builder, must control the type and
                       value of this attribute.
                       One way to have the control is to keep it privately.
    """
    def __init__(self, size):
        self.__size = size
