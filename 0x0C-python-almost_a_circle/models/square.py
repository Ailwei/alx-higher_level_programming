#!/usr/bin/python3
"""
define the square
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
        Initializes an instance of the Square class.

        Args:
            size (int): Size of the square.
            x (int, optional): x-coordinate of the square. Defaults to 0.
            y (int, optional): y-coordinate of the square. Defaults to 0.
            id (int, optional): The ID to assign to the instance. Defaults to None.
                Calls the super class with id, x, y, size, and size to utilize the logic of the __init__ method in the Rectangle class.
        """
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)
    def __str__(self):
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    @property
    def size(self):
        """Getter for the size attribute."""
        return self.width

    @size.setter
    def size(self, value):
        """Setter for the size attribute."""
        self.width = value
        self.height = value
def update(self, *args, **kwargs):
    """
    Assigns attributes based on both no-keyworded and keyworded arguments.

    Args:
        *args: No-keyworded arguments.
        **kwargs: Keyworded arguments.
    """
    if args:
        if len(args) > 0:
            self.id = args[0]
            if len(args) > 1:
                self.size = args[1]
                if len(args) > 2:
                    self.x = args[2]
                    if len(args) > 3:
                        self.y = args[3]
    else:
        if 'id' in kwargs:
            self.id = kwargs['id']
        if 'size' in kwargs:
            self.size = kwargs['size']
        if 'x' in kwargs:
            self.x = kwargs['x']
        if 'y' in kwargs:
            self.y = kwargs['y']

def to_dictionary(self):
        """Returns the dictionary representation of a Square instance."""
        return {
                'id': self.id,
                'width': self.width,
                'height': self.height,
                'x': self.x,
                'y': self.y
                }
