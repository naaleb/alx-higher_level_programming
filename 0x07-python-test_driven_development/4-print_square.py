#!/usr/bin/python3
"""
Prints a square with the character # module.
This module gives one function, print_square(size).
"""


def print_square(size):
    """ prints a square with the character # """
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if size > 0:
        print(("#" * size + "\n") * size, end="")
