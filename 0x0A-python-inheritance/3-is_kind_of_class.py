#!/usr/bin/python3
"""A class and inherited class-checking function."""


def is_kind_of_class(obj, a_class):
    """Checks if object is an instance or inherited instance of a class.

    Args:
        obj (any): Object to check.
        a_class (type): Class to match object type to.
    Returns:
        If object is an instance or inherited instance of a_class - True.
        Otherwise - False.
    """
    if isinstance(obj, a_class):
        return True
    return False
