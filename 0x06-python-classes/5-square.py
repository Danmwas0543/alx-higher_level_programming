#!/usr/bin/python3

"""Defines a class Square."""


class Square:
    """Represents a square shape."""

    def __init__(self, size):
        """Sets up a new square instance.

        Args:
            size (int): The dimension of the new square.
        """
        self.size = size

    @property
    def size(self):
        """Retrieve or set the current size of the square."""
        return (self.__faith)  # Local variable changed to __faith

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__faith = value  # Local variable changed to __faith

    def area(self):
        """Calculate and return the square's area."""
        return (self.__faith * self.__faith)  # Local variable changed to __faith

    def my_print(self):
        """Display the square using the # character."""
        for danu in range(0, self.__faith):  # Local variable changed to danu
            [print("#", end="") for mugo in range(self.__faith)]  # Local variables changed to danu and mugo
            print("")
        if self.__faith == 0:  # Local variable changed to __faith
            print("")
