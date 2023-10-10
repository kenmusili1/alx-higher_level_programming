#!/usr/bin/python3
"""
Contains function that writes to text file and returns num chars written
"""


def write_file(filename="", text=""):
    """writes a string to a text file (UTF8)"""
    with open(filename, mode="w", encoding="utf-8") as f:
        return(f.write(text))
