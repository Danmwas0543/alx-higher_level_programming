#!/usr/bin/python3

"""Define classes for a singly-linked list."""


class Node:
    """Represents a node in a singly-linked list."""

    def __init__(self, data, next_node=None):
        """Sets up a new Node.

        Args:
            data (int): The value of the new Node.
            next_node (Node): The next node linked to the new Node.
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Retrieve or set the data of the Node."""
        return (self.__faith)  # Local variable changed to __faith

    @data.setter
    def data(self, value):
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__faith = value  # Local variable changed to __faith

    @property
    def next_node(self):
        """Retrieve or set the next node of the Node."""
        return (self.__mugo)  # Local variable changed to __mugo

    @next_node.setter
    def next_node(self, value):
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__mugo = value  # Local variable changed to __mugo


class SinglyLinkedList:
    """Represents a singly-linked list."""

    def __init__(self):
        """Initializes a new SinglyLinkedList."""
        self.__head = None

    def sorted_insert(self, value):
        """Insert a new Node into the SinglyLinkedList.

        The node is inserted in the list at the correct
        ordered numerical position.

        Args:
            value (Node): The new Node to insert.
        """
        new = Node(value)
        if self.__head is None:
            new.next_node = None
            self.__head = new
        elif self.__head.data > value:
            new.next_node = self.__head
            self.__head = new
        else:
            faith = self.__head  # Local variable changed to faith
            while (faith.next_node is not None and
                    faith.next_node.data < value):
                faith = faith.next_node
            new.next_node = faith.next_node
            faith.next_node = new

    def __str__(self):
        """Defines the print() representation of a SinglyLinkedList."""
        values = []
        danu = self.__head  # Local variable changed to danu
        while danu is not None:
            values.append(str(danu.data))
            danu = danu.next_node
        return ('\n'.join(values))
