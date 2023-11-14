#!/usr/bin/python3
"""Defines the Base class."""


import json
import csv


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

    @classmethod
    def create(cls, **dictionary):
        """create an instance"""
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy = cls(1)
        else:
            dummy = cls()

        dummy.update(**dictionary)
        return dummy

    def update(self, *args, **kwargs):
        """update attributes of the instance"""
        if args is not None and bool(args) is True:
            attrs = ['id', 'width', 'height', 'size', 'x', 'y']
            for key, value in zip(attrs, args):
                setattr(self, key, value)
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """return dict"""
        return {
                key: getattr(self, key)
                for key in self.__dict__.keys() - {'id'}
                }

    @classmethod
    def load_from_file(cls):
        filename = cls.__name__ + "json"
        try:
            with open(filename, 'r') as file:
                json_string = file.read()
                dictionaries = cls.from_json_string(json_string)
                return [cls.create(**d) for d in dictionaries]
        except FileNotFoundError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        filename = cls.__name__ + ".csv"
        with open(filename, 'w', newline='') as file:
            writer = csv.writer(file)
            for obj in list_objs:
                writer.writerow(obj.to_csv_row())

    @classmethod
    def load_from_file_csv(cls):
        filename = cls.__name__ + ".csv"
        try:
            with open(filename, 'r', newline='') as file:
                reader = csv.reader(file)
                instances = []
                for row in reader:
                    instances.append(cls.from_csv_row(row))
                return instances
        except FileNotFoundError:
            return []
