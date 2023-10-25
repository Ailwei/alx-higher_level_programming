#!/usr/bin/python3
"""My square module"""


class Square:
    """Defines a square."""

    def __init__(self, size=0):
        """Initialize a square.

        Args:
            size (int): Length of a side of the square.
        """
        self.__size = size

    @property
    def size(self):
        """Get the size of the square.

        Returns:
            int: The length of a side of the square.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square.

        Args:
            value (int): The length of a side of the square.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    def area(self):
        """Calculate the area of the square.

        Returns:
            int: The area of the square (size squared).
        """
        return self.__size * self.__size

    def __le__(self, other):
        """Less than or equal to comparison based on areas."""
        return self.area() <= other.area()

    def __lt__(self, other):
        """Less than comparison based on areas."""
        return self.area() < other.area()

    def __ge__(self, other):
        """Greater than or equal to comparison based on areas."""
        return self.area() >= other.area()

    def __ne__(self, other):
        """Not equal comparison based on areas."""
        return self.area() != other.area()

    def __gt__(self, other):
        """Greater than comparison based on areas."""
        return self.area() > other.area()

    def __eq__(self, other):
        """Equal comparison based on areas."""
        return self.area() == other.area()
