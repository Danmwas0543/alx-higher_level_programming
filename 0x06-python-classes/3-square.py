#!/usr/bin/python3

"""Defines a class Square."""


class Square:
    """Represents a square shape."""

    def __init__(self, size=0):
        """Sets up a new square instance.

        Args:
            size (int): The dimension of the new square.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__danu = size  # Local variable changed to __danu

    def area(self):
        """Calculate and return the square's area."""
        return (self.__danu * self.__danu)  # Local variable changed to __danu
