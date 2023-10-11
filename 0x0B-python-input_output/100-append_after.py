#!/usr/bin/python3
"""
Represents a function that appends str after lines that include keyword
"""


def append_after(filename="", search_string="", new_string=""):
    """appends str after lines that include keyword (search_string)"""

    with open(filename, mode="r+", encoding="utf-8") as f:
        N_text = ""
        for line in f:
            N_text += line
            if search_string in line:
                N_text += new_string
        f.seek(0)
        f.write(N_text)
