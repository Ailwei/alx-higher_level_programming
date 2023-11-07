#!/usr/bin/python3
"""
student class
"""


class Student:
    """
    Represents a student with first name, last name, and age.

    Attributes:
        first_name (str): The first name of the student.
        last_name (str): The last name of the student.
        age (int): The age of the student.

    Methods:
        to_json(attrs=None):
            Retrieve a dictionary representation of a Student instance.

            Args:
                attrs (list): A list of attribute names
                to include in the dictionary.
                    If None, all attributes will be included.

            Returns:
                dict: A dictionary containing the specified or
                all attributes of the Student instance.
    """

    def __init__(self, first_name, last_name, age):
        """
        Initializes a new Student instance.

        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieve a dictionary representation of a Student instance.

        Args:
            attrs (list): A list of attribute names to
            include in the dictionary.
                If None, all attributes will be included.

        Returns:
            dict: A dictionary containing the specified or
            all attributes of the Student instance.
        """
        if attrs is None:
            return self.__dict__
        else:
            attr_dict = {}
            for attr in attrs:
                if hasattr(self, attr):
                    attr_dict[attr] = getattr(self, attr)
            return attr_dict
