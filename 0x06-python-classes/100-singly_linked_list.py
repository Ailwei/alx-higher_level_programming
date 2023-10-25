#!/usr/bin/python3
"""Module for a singly linked list."""


class Node:
    """Defines a node in a singly linked list."""

    def __init__(self, data, next_node=None):
        """Initializes a node with data and an optional reference to the next node.

        Args:
            data: The data to be stored in the node.
            next_node: Reference to the next node in the list.
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Gets the data attribute.

        Returns:
            int: The data stored in the node.

        Raises:
            TypeError: If data is not an integer.
        """
        return self.__data

    @data.setter
    def data(self, value):
        """Sets the data attribute.

        Args:
            value: The data to be stored in the node.

        Raises:
            TypeError: If data is not an integer.
        """
        if not isinstance(value, int):
            raise TypeError('data must be an integer')
        self.__data = value

    @property
    def next_node(self):
        """Gets the reference to the next node.

        Returns:
            Node: The reference to the next node in the list.

        Raises:
            TypeError: If the next_node is not a Node object.
        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """Sets the reference to the next node.

        Args:
            value: Reference to the next node in the list.

        Raises:
            TypeError: If the next_node is not a Node object.
        """
        if value is not None and not isinstance(value, Node):
            raise TypeError('next_node must be a Node object')


class SinglyLinkedList:
    """Defines a singly linked list."""

    def __init__(self):
        """Initializes an empty singly linked list."""
        self.head = None

    def __str__(self):
        """Creates a printable representation of the linked list.

        Returns:
            str: A string containing the data of each node in the list.
        """
        printsll = ""
        location = self.head
        while location:
            printsll += str(location.data) + "\n"
            location = location.next_node
        return printsll[:-1]

    def sorted_insert(self, value):
        """Inserts a new node with data in a sorted fashion.

        Args:
            value: The value to be stored in the new node.
        """
        new = Node(value)
        if not self.head:
            self.head = new
            return
        if value < self.head.data:
            new.next_node = self.head
            self.head = new
            return
        location = self.head
        while location.next_node and location.next_node.data < value:
            location = location.next_node
        if location.next_node:
            new.next_node = location.next_node
        location.next_node = new


