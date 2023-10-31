#!/usr/bin/python3
"""A class that represents a rectangle"""


class Rectangle:
    """A blueprint for a rectangle"""

    def __init__(self, width=0, height=0):
        """Create an instance of the Rectangle class.

        Args:
            initial_width (int): The initial width of the rectangle.
            initial_height (int): The initial height of the rectangle.

        Raises:
            TypeError: If width or height are not integers.
            ValueError: If width or height are less than zero.
        """
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """Get the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, width):
        """Set the width of the rectangle.

        Args:
            new_width (int): The new width of the rectangle.

        Raises:
            TypeError: If new_width is not an integer.
            ValueError: If new_width is less than zero.
        """
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        self.__width = width

    @property
    def height(self):
        """Get the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, height):
        """Set the height of the rectangle.

        Args:
            new_height (int): The new height of the rectangle.

        Raises:
            TypeError: If new_height is not an integer.
            ValueError: If new_height is less than zero.
        """
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__height = height

    def area(self):
        """Calculate and return the area of the rectangle."""
        return self.__width * self.__height

    def perimeter(self):
        """Calculate and return the perimeter of the rectangle."""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self) -> str:
        """Return a string representation of the rectangle as a diagram."""
        if self.__width == 0 or self.__height == 0:
            return ""
        rectangle_str = ""
        for _ in range(self.__height):
            rectangle_str += "#" * self.__width
            if _ < self.__height - 1:
                rectangle_str += "\n"
        return rectangle_str
