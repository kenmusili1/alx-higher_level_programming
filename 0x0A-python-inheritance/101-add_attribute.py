#!/usr/bin/python3

"""Function that adds attributes to an objects."""


def add_attribute(obj, Name, value):
    """
    Add a new attribute to an object if possible.
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, Name, value)
