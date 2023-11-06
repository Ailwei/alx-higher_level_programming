#!/usr/bin/python3
"""
Module 10-square
Defines a square and inherits from Rectangle
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Represents a square.
    Private instance attribute: size
    """

    def __init__(self, size):
        """
        Initializes the square.
        Args:
            - size: the size of the square
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        """
        Returns the square description.
        """
        return "[Square] {}/{}".format(self.__size, self.__size)
