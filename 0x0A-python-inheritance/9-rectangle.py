#!/usr/bin/python3
"""A rectangle class that inherits from Base Geometry."""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """A rectangle class using BaseGeometry."""

    def __init__(self, width, height):
        """Intialization of a new Rectangle.

        Args:
            width (int):Width of the new Rectangle.
            height (int): Height of the new Rectangle.
        """
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height

    def area(self):
        """Return an area of the rectangle."""
        return self.__width * self.__height

    def __str__(self):
        """Return print() and str() representation of a Rectangle."""
        string = "[" + str(self.__class__.__name__) + "] "
        string += str(self.__width) + "/" + str(self.__height)
        return string