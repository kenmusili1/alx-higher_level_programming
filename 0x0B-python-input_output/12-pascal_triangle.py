#!/usr/bin/python3
"""
Represents function that returns int lists of pascal triangle of any given size
"""


def pascal_triangle(n):
    """
    Returns a list of lists of integers
    representing the Pascal triangle of n
    """
    if n <= 0:
        return []
    triangle = []
    l = []
    for z in range(n):
        row = []
        for y in range(z + 1):
            if z == 0 or y == 0 or z == y:
                row.append(1)
            else:
                row.append(l[y] + l[y - 1])
        l = row
        triangle.append(row)
    return triangle
