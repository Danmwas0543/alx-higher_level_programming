#!/usr/bin/python3

"""Defines a class Square."""


class Square:
    """Represents a square shape."""

    def __init__(self, size=0):
        """Sets up a new square instance.

        Args:
            size (int): The dimension of the new square.
        """
        self.size = size

    @property
    def size(self):
        """Retrieve or set the current size of the square."""
        return self.__danu  # Local variable changed to __danu

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__danu = value  # Local variable changed to __danu

    def area(self):
        """Calculate and return the square's area."""
        return (self.__danu * self.__danu)  # Local variable changed to __danu
