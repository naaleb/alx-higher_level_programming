#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    cout = 0
    for i in range(x):
        try:
            print("{}".format(my_list[i], end=""))
            cout += 1
            except IndexError:
                break
    print("")
    return (count)
