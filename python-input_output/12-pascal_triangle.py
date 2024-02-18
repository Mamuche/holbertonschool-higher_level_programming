#!/usr/bin/python3
"""function for def pascal_triangle"""


def pascal_triangle(n):
    """returns a lists of integers representing the Pascals triangle of n"""
    if n <= 0:
        return []

    """initializes the variable with a list containing a list
    [1] is the first line of the triangle"""
    triangle = [[1]]

    for x in range(1, n):
        row = [1]
        for y in range(1, x):
            """Add to row the sum of the two numbers
            directly above it in the triangle"""
            row.append(triangle[x-1][y-1] + triangle[x-1][y])
        """Add 1 to the end of the line, as each line of
        Pascal's triangle begins and ends with 1."""
        row.append(1)
        """Add row to the triangle list,
        which gradually builds the triangle."""
        triangle.append(row)
    return triangle
