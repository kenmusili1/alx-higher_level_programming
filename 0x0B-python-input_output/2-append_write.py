#!/usr/bin/python3
"""
Contains function that writes to text file and returns num chars written
"""


def append_write(filename="", text=""):
    """
    appends a string at the end of a text file (UTF8)
    """
    with open(filename, "a", encoding="utf-8") as f:
        f.write(text)
    return len(text)
