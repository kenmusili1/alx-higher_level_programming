#!/usr/bin/python3
"""
Represents function that writes Python obj to file using JSON represenation
"""
import json


def save_to_json_file(my_obj, filename):
    """
    Writes Python obj to file, using JSON represenation
    """
    with open(filename, 'w', encoding="utf-8") as f:
        json.dump(my_obj, f)
