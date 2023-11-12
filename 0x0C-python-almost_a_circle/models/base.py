#!/usr/bin/python3
"""
define base class
"""
import json
import csv
import turtle
from collections import OrderedDict


class Base:
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initializes an instance of the Base class.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod 
    def to_json_string(list_dictionaries):
        """
        Returns the JSON string representation of a list of dictionaries.

        Args:
            list_dictionaries (list): A list of dictionaries.

        Returns:
            str: The JSON string representation of the list of dictionaries.
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Writes the JSON string representation of a list of objects to a file.

        Args:
            cls: The class (Base or its subclass).
            list_objs (list): A list of instances that inherit from Base.

        Returns:
            None
        """
        filename = "{}.json".format(cls.__name__)
        list_dictionaries = []
        if list_objs is None:
            for objs in list_objs:
                dictionary = obj.to_dictionary()
                list_objs.append(dictionary)
        json_string = Base.to_json_string(list_dictionaries)

        with open(filename, 'w') as f:
            if list_objs is None:
                f.write("[]")
            else:
                f.write(json_string)

def from_json_string(json_string):
    """
    Returns the list of dictionaries represented by a JSON string.
    """
    if json_string is None or json_string == "":
        return []
    else:
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        Returns an instance with all attributes set based on the provided dictionary.

        Args:
            cls: The class (Base or its subclass).
            **dictionary: A dictionary containing attribute values for the instance.

        Returns:
            instance: An instance of the class with attributes set based on the dictionary.
        """
        if cls.__name__ == "Rectangle":
            dummy_instance = cls(1,1)
        elif cls.__name__ == "Square":
            dummy_instance = cls(1)
        else:
            raise ValueEroor("Unsupported class")
        dummy_instance.update(**dictionary)
        return dummy_instance
    
    @classmethod
    def load_from_file(cls):
        """
        Returns a list of instances based on the contents of a JSON file.

        Returns:
            list: A list of instances.
        """
        filename = "{}.json".format(cls.__name__)

        try:
            with open(filename, 'r') as file:
                json_string = file.read()
        except FileNotFoundError:
            return []

        list_dictionaries = cls.from_json_string(json_string)
        instances = [cls.create(**dic) for dic in list_dictionaries]
        return instances

    @staticmethod
    def to_csv_row(dictionary):
        """Converts a dictionary to a CSV row."""
        return [str(value) for value in dictionary.values()]

    @staticmethod
    def from_csv_row(row):
        """Converts a CSV row to a dictionary."""
        return {key: int(value) for key, value in zip(["id", "width", "height", "x", "y"], row)}

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """
        Serializes instances to a CSV file.

        Args:
            cls: The class (Base or its subclass).
            list_objs (list): A list of instances that inherit from Base.

        Returns:
            None
        """

        filename = cls.__name__ + ".csv"
        print(f"Saving to file: {filename}")
        with open(filename, mode='w', newline='') as file:
            writer = csv.writer(file)
            if list_objs is not None:
                for obj in list_objs:
                    writer.writerow(cls.to_csv_row(obj.to_dictionary()))
            else:
                writer.writerow([])

    @classmethod
    def load_from_file_csv(cls):
        """Deserializes objects from a CSV file."""
        filename = cls.__name__ + ".csv"
        print(f"Loading from file: {filename}")
        objects = []
        try:
            with open(filename, mode='r') as file:
                reader = csv.reader(file)
                for row in reader:
                    if row:
                        obj_dict = cls.from_csv_row(row)
                        obj = cls.create(**obj_dict)
                        objects.append(obj)
        except FileNotFoundError:
            pass  # File not found, return an empty list
        return objects

    @staticmethod
    def draw(list_rectangles, list_squares):
        """
        Opens a window and draws all Rectangles and Squares using Turtle graphics.

        Args:
            list_rectangles (list): A list of Rectangle instances.
            list_squares (list): A list of Square instances.

        Returns:
            None
        """
        screen = turtle.Screen()
        screen.bgcolor("white")

        for rect in list_rectangles:
            turtle.penup()
            turtle.goto(rect.x, rect.y)
            turtle.pendown()
            turtle.forward(rect.width)
            turtle.left(90)
            turtle.forward(rect.height)
            turtle.left(90)
            turtle.forward(rect.width)
            turtle.left(90)
            turtle.forward(rect.height)
            turtle.left(90)

        for square in list_squares:
            turtle.penup()
            turtle.goto(square.x, square.y)
            turtle.pendown()
            for _ in range(4):
                turtle.forward(square.size)
                turtle.left(90)

        turtle.done()
