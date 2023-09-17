#!/usr/bin/python3
i = 0

for c in range(ord('z'), ord('a') - 1, -1):
    char_to_print = chr(c - i)
    print("{}".format(char_to_print), end="")
    i = 32 if i == 0 else 0
