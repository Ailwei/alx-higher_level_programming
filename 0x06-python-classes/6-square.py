#!/usr/bin/python3
"""This module contains the Square class"""


class Square:
    """
    Represents a 2D square with four equal and perpendicular sides.

    Args:
        size (int): The size of the square.

    Attributes:
        __size (int): A private instance attribute.
    """

    def __init__(self, size=0):
        """
        Initializes a square with the given size.

        Args:
            size (int): The size of the square.
        """

        self.__size = size

    @property
    def size(self):
        """
        Retrieve the size of the square.

        Returns:
            int: The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Set the size of the square.

        Args:
            value (int): The new size of the square.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than zero.
        """

        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    def area(self):
        """
        Calculate the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2

    def my_print(self):
        """
        Print a 2D representation of the square with the '#' symbol.
        """
        if self.__size > 0:
            for i in range(self.__size):
                for j in range(self.__size):
                    print('#', end='')
                print()
        else:
            print()
