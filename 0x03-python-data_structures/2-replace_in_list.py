#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    if not isinstance(my_list, list):
        return

    for i in reversed(my_list):
        if isinstance(i, int):
            print("{:d}".format(i))
