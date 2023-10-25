#!/usr/bin/python3
"""A module with a MagicClass"""

import math


class MagicClass:
    """A class that defines a MagicClass.

    Attributes:
        __radius (float): The radius of the MagicClass instance.
    """

    def __init__(self, radius=0):
        """Initialize a MagicClass instance with a given radius.

        Args:
            radius (int or float): The radius of the MagicClass.

        Raises:
            TypeError: If the radius is not a number (int or float).
        """
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')
        self.__radius = radius

    def area(self):
        """Calculate the area of the MagicClass instance.

        Returns:
            float: The area of the MagicClass instance.
        """
        return self.__radius ** 2 * math.pi

    def circumference(self):
        """Calculate the circumference of the MagicClass instance.

        Returns:
            float: The circumference of the MagicClass instance.
        """
        return 2 * math.pi * self.__radius
