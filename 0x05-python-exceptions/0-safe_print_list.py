#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    """Print x number of elements from a list.

    Parameters:
        my_list (list): The list containing elements to be printed.
        x (int): The number of elements from my_list to be printed.

    Returns:
        int: The count of elements that were successfully printed.
    """

    count = 0
    for i in range(x):
        try:
            print("{}".format(my_list[i]), end="")
            count += 1
        except IndexError:
            break
    print("")
    return (count)
