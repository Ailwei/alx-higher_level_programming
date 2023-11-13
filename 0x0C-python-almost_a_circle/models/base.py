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

    @classmethod
    def save_to_file(cls, list_objs):
        """write the json representation of list_obj to a file"""
        filename = cls.__name__ + "json"
        with open(filename, 'w') as file:
            if list_objs is None:
                file.write("[]")
            else:
                json_dicts = (obj.to_dictionary() for obj in list_objs)
                json_string = cls.to_json_string(list(json_dicts))
                file.write(json_string)

    @staticmethod
    def from_json_string(json_string):
        """Return the list of the JSON string representation json_striing"""
        if json_string is None or not json_string:
            return []
        return json.loads(json_string)
