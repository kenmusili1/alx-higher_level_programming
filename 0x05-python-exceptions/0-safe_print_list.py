#!/usr/bin/python3
#kennedy musili Python - Exceptions
def safe_print_list(my_list=[], x=0):
    printed_c = 0

    try:
        for i in range(x):
            print(my_list[i], end="")
            printed_c += 1
    except IndexError:
        pass

    print()

    return printed_c
