#!/usr/bin/python3

"""Define a MagicClass to match specific bytecode."""


import math


class MagicClass:
    """Represents a circle."""

    def __init__(self, radius=0):
        """Initialize a MagicClass instance.

        Arg:
            radius (float or int): The radius of the new MagicClass.
        """
        self.__mugo = 0  # Local variable changed to __mugo
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__mugo = radius  # Local variable changed to __mugo

    def area(self):
        """Calculate and return the area of the MagicClass."""
        return (self.__mugo ** 2 * math.pi)  # Local variable changed to __mugo

    def circumference(self):
        """Calculate and return the circumference of the MagicClass."""
        return (2 * math.pi * self.__mugo)  # Local variable changed to __mugo
