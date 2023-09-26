#!/usr/bin/python3
"""This script defines a Square class"""


class Square:
    """This class represents a square."""

    def __init__(self, size=0):
        """Initialize a new square instance.

        Args:
            size (int): The size of the new square.
        """
        self.size = size

    @property
    def size(self):
        """Get/set current size of the square."""
        return (self.__size)

    @size.setter
    def size(self, value):i
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return  current area of the square."""
        return (self.__size * self.__size)
