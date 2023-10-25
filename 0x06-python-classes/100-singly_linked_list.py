#!/usr/bin/python3

class Node:
    """
    Defines a node of a singly linked list.

    Attributes:
        data (int): The data stored in the node.
        next_node (Node): Reference to the next node in the list.
    """

    def __init__(self, data, next_node=None):
        """
        Initializes a new Node instance.

        Args:
            data (int): The data to be stored in the node.
            next_node (Node): Reference to the next node in the list.
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """
        Get the data stored in the node.

        Returns:
            int: The data stored in the node.

        Raises:
            TypeError: If data is not an integer.
        """
        return self.__data

    @data.setter
    def data(self, value):
        """
        Set the data stored in the node.

        Args:
            value (int): The data to be stored in the node.

        Raises:
            TypeError: If data is not an integer.
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """
        Get the reference to the next node in the list.

        Returns:
            Node: The reference to the next node in the list.

        Raises:
            TypeError: If the next_node is not a Node object.
        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """
        Set the reference to the next node in the list.

        Args:
            value (Node): Reference to the next node in the list.

        Raises:
            TypeError: If the next_node is not a Node object.
        """
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value
