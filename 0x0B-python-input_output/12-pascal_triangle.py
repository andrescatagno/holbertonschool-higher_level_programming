#!/usr/bin/python3
"""
Contains the pascal triangle
"""


def pascal_triangle(n):
    """returns a list of lists of integers
    representing the Pascal's triangle of n"""

    if n < 0:
        return[]

    triangle = [[1]]
    while len(triangle) != n:
        tri = triangle[-1]
        tmp = [1]
        for i in range(len(tri) - 1):
            tmp.append(tri[i] + tri[i + 1])
        tmp.append(1)
        triangle.append(tmp)
    return(triangle)
