#!/usr/bin/python3
class Rectangle:
    """
    This class defines a rectangle and
    provides methods for accessing and modifying its dimensions.
    """

    def __init__(self, width=0, height=0):
        """
        Initializes a new instance of the Rectangle class.

        :param width: The width of the rectangle (default is 0).
        :param height: The height of the rectangle (default is 0).
        """
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """
        Getter method for retrieving the width of the rectangle.

        :return: The width of the rectangle.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Setter method for setting the width of the rectangle.

        :param value: The new width value to set.
        :raises TypeError: If the value is not an integer.
        :raises ValueError: If the value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        Getter method for retrieving the height of the rectangle.

        :return: The height of the rectangle.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Setter method for setting the height of the rectangle.

        :param value: The new height value to set.
        :raises TypeError: If the value is not an integer.
        :raises ValueError: If the value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
