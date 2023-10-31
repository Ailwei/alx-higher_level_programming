#!/usr/bin/python3

class Rectangle:
    """
    This class defines a rectangle.

    Attributes:
    - width (int): The width of the rectangle.
    - height (int): The height of the rectangle.

    Public Class Attribute:
    - number_of_instances (int): Keeps track of the number of instances created.

    Methods:
    - __init__(self, width=0, height=0): Initializes a new Rectangle instance.
    - area(self): Returns the area of the rectangle.
    - perimeter(self): Returns the perimeter of the rectangle.
    - __str__(self): Returns a string representation of the rectangle.
    - __repr__(self): Returns a string representation that can recreate the instance.
    - __del__(self): Displays a message and updates the number_of_instances when an instance is deleted.
    """

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """
        Initializes a new Rectangle instance.

        Args:
        - width (int): The width of the rectangle.
        - height (int): The height of the rectangle.
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Get the width of the Rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width of the Rectangle, validating it's an integer and >= 0."""
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
        """Set the height of the Rectangle, validating it's an integer and >= 0."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Return the area of the Rectangle."""
        return self.__width * self.__height

    def perimeter(self):
        """Return the perimeter of the Rectangle."""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (2 * self.__width + 2 * self.__height)

    def __str__(self):
        """Return a string representation of the Rectangle using '#' characters."""
        if self.__width == 0 or self.__height == 0:
            return ""
        rectangle_str = ""
        for i in range(self.__height):
            rectangle_str += "#" * self.__width
            if i < self.__height - 1:
                rectangle_str += "\n"
        return rectangle_str

    def __repr__(self):
        """Return a string representation that can recreate the instance."""
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """Display a message and update the number_of_instances when an instance is deleted."""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
