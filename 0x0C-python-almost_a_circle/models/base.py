#!/usr/bin/python3
"""Defines the Base class."""


import json


class Base:
    """The base class for all other classes in this project."""

    __nb_objects = 0  # private class attribute

    def __init__(self, id=None):
        """Initialize an instance of the Base class.

        Args:
            id (int, optional): The ID to assign to the instance.
                Defaults to None.

        Note:
            If `id` is not None, assign it to the public instance
            attribute `id`. Otherwise, increment the private class
            attribute `__nb_objects` and assign the new value to the
            public instance attribute `id`.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """return the json string representation of dictionary list"""
        if list_dictionaries is None or not list_dictionaries:
            return "[]"
        return json.dumps(list_dictionaries)
