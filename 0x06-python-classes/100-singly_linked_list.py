#!/usr/bin/python3
'''A module for working with singly linked lists.
'''


class Node:
    '''Represents a node in a singly linked list.
    '''
    def __init__(self, data, next_node=None):
         '''Initializes a Node with a given data and next link.

        Args:
            data (int): The data of the Node.
            next_node (Node): The Node next to this Node.
        '''
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
           '''Retrieves the data of this Node.

        Returns:
            int: The data of this Node.
        '''
        return self.__data

    @data.setter
    def data(self, value):
        '''Updates the data of this Node.

        Args:
            value (int): The new data of this Node.
        '''
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
         '''Retrieves the Node next to this Node.

        Returns:
            Node: The Node next to this Node.
        '''
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
         '''Updates the next node of this Node.

        Args:
            value (Node): The new node next to  this Node.
        '''
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    def __init__(self):
        self.__head = None

    def sorted_insert(self, value):
        new_node = Node(value)
        if self.__head is None or value < self.__head.data:
            new_node.next_node = self.__head
            self.__head = new_node
            return

        current = self.__head
        while current.next_node is not None and current.next_node.data < value:
            current = current.next_node

        new_node.next_node = current.next_node
        current.next_node = new_node

    def __str__(self):
        result = []
        current = self.__head
        while current:
            result.append(str(current.data))
            current = current.next_node
        return '\n'.join(result)
