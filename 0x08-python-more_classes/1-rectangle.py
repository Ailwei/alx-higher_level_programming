#!/usr/bin/python3

"""the function that define the rectangle"""


class Rectangle:
    """this represent rectangle class"""

    def __init__(self, width=0, height=0):
        """
        Inialiazing this rectangle class
        Args:
            width: represents the width of the rectangle
            height: represents the height of the rectangle
        Raise:
            TypeError: if value is not integer
            ValueEroor: if value is less than 0
        """
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """attributer getter for width attribut"""
        return self.__width

    @width.setter
    def width(self, value):
        """sets width attribute"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("Value must be an integer >= 0")
        self.__width = value

    @property
    def height(self):
        """retrieve height attribute"""
        return self.__height

    @height.setter
    def height(self, value):
        """sets height attribute"""
        if not isinstance(value, int):
            raise TypeError("Height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
