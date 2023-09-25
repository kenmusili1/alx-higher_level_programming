#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    printed_c = 0

    try:
        for i in my_list:
            if printed_c < x:
                print('{}'.format(my_list[printed_c]), end='')
                printed_c += 1

        print()
    except TypeError:
        pass
    finally:
        return printed_c
