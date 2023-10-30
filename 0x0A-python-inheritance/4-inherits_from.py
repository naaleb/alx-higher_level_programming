#!/usr/bin/python3

"""An inherited function to check  class"""


def inherits_from(obj, a_class):
    """Checks if object is an inherited instance of a class.

    Args:
        obj (any): The object to check.
        a_class (type): The class to match the type of object.
    Returns:
        If object is an inherited instance of a_class - True.
        Otherwise - False.
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
