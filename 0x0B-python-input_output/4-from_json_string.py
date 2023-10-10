#!/usr/bin/python3
"""
Represents function that returns python data structure from JSON string
"""
import json


def from_json_string(my_str):
    """
    returns Python data structure represented by a JSON string
    """
    return json.loads(my_str)
