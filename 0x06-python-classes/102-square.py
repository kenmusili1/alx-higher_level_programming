#!/usr/bin/python3
"""Define a class Square."""


class Square:
    """Represent a square."""

    def __init__(self, size=0):
        """Initialize a new square.

        Args:
            size (float or int): The size of the new square.
        """
        self.size = size

    @property
    def size(self):
        """Retrieve the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square.

        Args:
            value (float or int): The size to set.

        Raises:
            TypeError: If value is not a number (float or integer).
            ValueError: If value is less than 0.
        """
        if not isinstance(value, (float, int)):
            raise TypeError("size must be a number")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return the current square area."""
        return self.__size ** 2

    def __eq__(self, other):
        """Check if two squares have equal areas."""
        return self.area() == other.area()

    def __ne__(self, other):
        """Check if two squares have unequal areas."""
        return self.area() != other.area()

    def __lt__(self, other):
        """Check if one square has a smaller area than the other."""
        return self.area() < other.area()

    def __le__(self, other):
        """Check if one square has a smaller or equal area to the other."""
        return self.area() <= other.area()

    def __gt__(self, other):
        """Check if one square has a larger area than the other."""
        return self.area() > other.area()

    def __ge__(self, other):
        """Check if one square has a larger or equal area to the other."""
        return self.area() >= other.area()
