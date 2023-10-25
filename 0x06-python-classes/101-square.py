#!/usr/bin/python3
"""My square module."""


class Square:
    """Defines a square."""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize a square with a specified size and position.

        Args:
            size (int): The length of a side of the square.
            position (tuple): The position of the square (x, y).
        """
        self.size = size
        self.position = position

    def __str__(self):
        """Return a string representation of the square."""
        return self.pos_print()[:-1]

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

    @property
    def position(self):
        """Get the position of the square.

        Returns:
            tuple: The position coordinates (x, y).

        Raises:
            TypeError: If the position is not a tuple of two positive integers.
        """
        return self.__position

    @position.setter
    def position(self, value):
        """Set the position of the square.

        Args:
            value (tuple): The position coordinates as a tuple of two positive integers.

        Raises:
            TypeError: If value is not a tuple or if any integer in the tuple is less than 0.
        """
        if not isinstance(value, tuple):
            raise TypeError('position must be a tuple of 2 positive integers')
        if len(value) != 2:
            raise TypeError('position must be a tuple of 2 positive integers')
        if len([i for i in value if isinstance(i, int) and i >= 0]) != 2:
            raise TypeError('position must be a tuple of 2 positive integers')
        self.__position = value

    def area(self):
        """Calculate the area of the square.

        Returns:
            int: The area of the square (size squared).
        """
        return self.__size * self.__size

    def pos_print(self):
        """Generate the string representation of the square with the specified position."""
        pos = ""
        if not self.size:
            return "\n"
        for _ in range(self.position[1]):
            pos += "\n"
        for _ in range(self.size):
            pos += " " * self.position[0]
            pos += "#" * self.size
            pos += "\n"
        return pos

    def my_print(self):
        """Print the square with the specified position."""
        print(self.pos_print(), end="")
