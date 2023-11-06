#!/usr/bin/python3
"""
this define geomentry class
"""


class BaseGeometry:
    """
    raise:
         :that raises an Exception with the message area() is not implemented
    """
    def area(self):
        """
        not yet implemented
        """

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        validates integer
        Args:
            :name
            :value
        Raises:
               TypeError: if the value is not integer
               ValueError: if the value is less than or equal
        """

        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
