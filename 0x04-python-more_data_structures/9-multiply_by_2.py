#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    new_dictionary = {}
    
    for key, i in a_dictionary.items():
        new_dictionary[key] = i * 2
    
    return new_dictionary
