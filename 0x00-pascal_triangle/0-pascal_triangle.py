#!/usr/bin/python3
"""Triangle Triangle"""


def pascal_triangle(n):
    """Triangle"""
    if n <= 0:
        return []
    pascal_triangle = [[1]]
    for row_number in range(1, n):
        row = [1]
        for j in range(1, row_number):
            element = (
                pascal_triangle[row_number - 1][j - 1]
                + pascal_triangle[row_number - 1][j]
            )
            row.append(element)
        row.append(1)
        pascal_triangle.append(row)

    return pascal_triangle
