#!/usr/bin/python3
"""
this define the rectangle class
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    Represents a rectangle using BaseGeometry
    """
    def __init__(self, width, height):
        """
        initialize a rectangle instance with the specified width and height
        Args:
            width (int)
            height (int)
        Raises:
              TypeError: if width or height is not positive int
        """

        super().__init__()
        self.__width = 0
        self.__height = 0
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """
        Calculate the area of the rectangle

        Returns:
               int: The area of the rectangle
        """
        return self.__width * self.__height

    def __str__(self):
        """
        return a string representation of the string

        return:
              str: A string in the format "[Rectangle] <width>/<height>".
        """

        return "[Rectangle] {}/{}".format(self.__width, self.__height)
