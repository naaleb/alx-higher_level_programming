#!/usr/bin/python3
"""Defining Pascal's Triangle function."""


def pascal_triangle(n):
    """Represents Pascal's Triangle of size n.

    Returns an empty list if n <= 0.
    """
    if n <= 0:
        return []

    triangles = [[1]]
    while len(triangles) != n:
        tri = triangles[-1]
        tmp = [1]
        for i in range(len(tri) - 1):
            tmp.append(tri[i] + tri[i + 1])
        tmp.append(1)
        triangles.append(tmp)
    return triangles
