#!usr/bin/python3
"""moulde of pascal tringle"""


def pascal_triangle(n):
    """Returns a pascal tringle of n"""
    if n <= 0:
        return []

    tringle = [[1]]
    for r in range(n - 1):
        row = [1]

        for num in range(r):
            row.append(tringle[r][num] + tringle[r][num+1])

        row.append(1)
        tringle.append(row)

    return tringle
