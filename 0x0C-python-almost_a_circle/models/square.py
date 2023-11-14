#!/usr/bin/python3
"""Defines the Square class."""

from models.rectangle import Rectangle
import csv


class Square(Rectangle):
    """Represents a square."""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialize a Square instance.

        Args:
            size (int): The size of the square.
            x (int, optional): The x-coordinate of the square. Defaults to 0.
            y (int, optional): The y-coordinate of the square. Defaults to 0.
            id (int, optional): The ID of the square. Defaults to None.
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Getter method for size."""
        return self.width

    @size.setter
    def size(self, value):
        """Setter method for size."""
        self.width = value
        self.height = value

    def __str__(self):
        """Return a string representation of the Square."""
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width
        )

    def update(self, *args, **kwargs):
        """ assignn attributes to the instances"""
        if args:
            attributes = ["id", "size", "x", "y"]
            for i, arg in enumerate(args):
                setattr(self, attributes[i], arg)
        elif kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """return a string represatatrion of the square"""
        return {
                'id': self.id,
                'size': self.width,
                'x': self.x,
                'y': self.y
                }

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

    @classmethod
    def from_csv_row(cls, row):
        return cls(*map(int, row[1:]), id=int(row[0]))
