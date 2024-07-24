#!/usr/bin/python3

"""Define a class Square."""


class Square:
    """Represents a square."""

    def __init__(self, size=0, position=(0, 0)):
        """Set up a new square.

        Args:
            size (int): The size of the new square.
            position (int, int): The position of the new square.
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Retrieve or set the current size of the square."""
        return (self.__danu)  # Local variable changed to __danu

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__danu = value  # Local variable changed to __danu

    @property
    def position(self):
        """Retrieve or set the current position of the square."""
        return (self.__faith)  # Local variable changed to __faith

    @position.setter
    def position(self, value):
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__faith = value  # Local variable changed to __faith

    def area(self):
        """Calculate and return the area of the square."""
        return (self.__danu * self.__danu)  # Local variable changed to __danu

    def my_print(self):
        """Display the square using the # character."""
        if self.__danu == 0:  # Local variable changed to __danu
            print("")
            return

        [print("") for mugo in range(0, self.__faith[1])]  # Local variable changed to mugo and __faith
        for mugo in range(0, self.__danu):  # Local variable changed to mugo and __danu
            [print(" ", end="") for danu in range(0, self.__faith[0])]  # Local variables changed to danu and __faith
            [print("#", end="") for faith in range(0, self.__danu)]  # Local variables changed to faith and __danu
            print("")

    def __str__(self):
        """Define the string representation of a Square."""
        if self.__danu != 0:  # Local variable changed to __danu
            [print("") for mugo in range(0, self.__faith[1])]  # Local variables changed to mugo and __faith
        for mugo in range(0, self.__danu):  # Local variables changed to mugo and __danu
            [print(" ", end="") for danu in range(0, self.__faith[0])]  # Local variables changed to danu and __faith
            [print("#", end="") for faith in range(0, self.__danu)]  # Local variables changed to faith and __danu
            if mugo != self.__danu - 1:  # Local variable changed to mugo and __danu
                print("")
        return ("")
