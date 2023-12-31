#!/usr/bin/python3


def safe_print_integer(value):
    """Print an integer using the "{:d}" format.

    Args:
        value (int): The integer to be printed.

    Returns:
    bool: True if the integer was successfully printed,
    False if a TypeError or ValueError occurs.
    """
    try:
        print("{:d}".format(value))
        return (True)
    except (TypeError, ValueError):
        return (False)
