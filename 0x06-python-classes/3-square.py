#!/usr/bin/python3
"""A script that defines a Square class."""


class Square:
    """This represent a square."""

    def __init__(self, size=0):
        """Initialize a new square class.

        Args:
            size (int): The size of the square.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Return current area of the square."""
        return (self.__size * self.__size)
