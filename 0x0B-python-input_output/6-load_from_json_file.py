#!/usr/bin/python3
"""
Represents function that creates a Python obj from JSON file
"""
import json


def load_from_json_file(filename):
    """
    creates an Object from a “JSON file”
    """
    with open(filename, encoding="utf-8") as f:
        return json.load(f)
