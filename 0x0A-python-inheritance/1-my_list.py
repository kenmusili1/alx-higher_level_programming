#!/usr/bin/python3

"""Defines an inherited list class MyList."""


class MyList(list):
    """Custom list class that prints the list in sorted order."""

    def print_sorted(self):
        """Print the list in ascending sorted order."""
        print(sorted(self))
