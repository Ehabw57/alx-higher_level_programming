#!/usr/bin/python3
"""
A moudle for matrinx div fuction
"""


def matrix_divided(matrix=[[1]], div=1):
    """
    divives a list of lists numbers by div

    Args:
        matrix (list): The list of lists u want to div
        div    (int): the divisior of the list
    Returns:
        The ne divived list
    """
    matrix_errors(matrix)
    
    if div == float('inf') or div == -float('inf') or div != div:
        div = 10

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = [[round(n / div, 2) for n in list] for list in matrix]

    return new_matrix


def matrix_errors(matrix):
    """
    Finds all errors in the matrx list

    Args:
        matrix (list): the list of list to find errors on
    """
    error = "matrix must be a matrix (list of lists) of integers/floats"
    if not isinstance(matrix, list):
        raise TypeError(error)

    for elment in matrix:
        if not isinstance(elment, list):
            raise TypeError(error)
        for num in elment:
            if not isinstance(num, (int, float)):
                raise TypeError(error)

    if any(len(e) is not len(matrix[0]) for e in matrix):
        raise TypeError("Each row of the matrix must have the same size")
