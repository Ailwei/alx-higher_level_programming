#!/usr/bin/python3
"""
define pascal rectangle
"""


def pascal_triangle(n):
    """
    Generate Pascal's triangle up to the nth row.

    Args:
        n (int): The number of rows to generate in Pascal's triangle.

    Returns:
        list: A list of lists of integers representing Pascal's triangle up to the nth row.
              Returns an empty list if n is less than or equal to 0.
    """
    if n <= 0:
        return []

    triangle = []
    for i in range(n):
        row = []
        for j in range(i + 1):
            if j == 0 or j == i:
                # The first and last elements of each row are 1
                row.append(1)
            else:
                # Other elements are the sum of the two elements above in the previous row
                row.append(triangle[i - 1][j - 1] + triangle[i - 1][j])
        triangle.append(row)

    return triangle
