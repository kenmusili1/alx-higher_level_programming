#!/usr/bin/python3

def complex_delete(a_dictionary, value):
    keys = []
    for l, n in a_dictionary.items():
        if n == value:
            keys.append(l)

    for l in keys:
        del a_dictionary[l]

    return a_dictionary
