#!/usr/bin/python3
"""A class to represent a Rectangle."""


class Rectangle:
    """Definition of a rectangle class."""

    def __init__(self, width=0, height=0):
        """Create a new Rectangle instance.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Get the width of the Rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get the height of the Rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Calculate and return the area of the Rectangle."""
        return self.__width * self.__height

    def perimeter(self):
        """Calculate and return the perimeter of the Rectangle."""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width * 2) + (self.__height * 2)

    def __str__(self):
        """Returns a printable representation of the rectangle.

        Represent the Rectangle with the # character.
        """
        if self.__width == 0 or self.__height == 0:
            return ""
        rect_angle = []
        for _ in range(self.__height):
            [rect.append('#') for _ in range(self.__width)]
            if _ != self.__height - 1:
                rect_angle.append("\n")
        return "".join(rect_angle)

    def __repr__(self):
        """Returns the string that represent the Rectangle."""
        return f"Rectangle({self.__width}, {self.__height})"
