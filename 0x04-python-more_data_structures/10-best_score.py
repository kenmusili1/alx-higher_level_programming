#!/usr/bin/python3

def best_score(a_dictionary):
    if a_dictionary:
        y = max(sorted(a_dictionary.values()))
        for x, z in a_dictionary.items():
            if y == z:
                return (x)
    else:
        return (None)
