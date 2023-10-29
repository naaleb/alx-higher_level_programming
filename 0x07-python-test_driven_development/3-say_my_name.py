#!/usr/bin/python3
"""
A prints My name is <first name> <last name> module.
This module gives one function, say_my_name.
"""


def say_my_name(first_name, last_name=""):
    """ Prints first name and last name """
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")
    print("My name is", first_name, last_name)
