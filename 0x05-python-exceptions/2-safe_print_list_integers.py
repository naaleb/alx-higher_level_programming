#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    """Print integers of first x elements of a list.

    Args:
        my_list (list): list to print elements.
        x (int): The number of elements to print from my list.

    Returns:
        The number of elements printed.
    """
    count = 0
    for i in range(0, x):
        try:
            print("{:d}".format(my_list[i]), end="")
            count += 1
        except (ValueError, TypeError):
            continue
    print("")
    return (count)
