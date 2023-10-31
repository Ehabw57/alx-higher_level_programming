#!/usr/bin/python3
"""
A moudle for matrinx div fuction
"""


def matrix_divided(matrix, div):
    """
    divives a list of lists numbers by div

    Args:
        matrix (list): The list of lists u want to div
        div    (int): the divisior of the list
    Returns:
        The ne divived list
    """
    matrix_errors(matrix)

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = [[round(number / div, 2) for number in list] for list in matrix]

    return new_matrix


def matrix_errors(matrix):
    """
    Finds all errors in the matrx list

    Args:
        matrix (list): the list of list to find errors on
    """
    error = "matrix must be a matrix (list of lists) of integers/floats"
    if not isinstance(matrix, list) or not any(isinstance(e, list) for e in matrix):
        raise TypeError(error)

    if not any(isinstance(i, (int, float)) for e in matrix for i in e):
        raise TypeError(error)

    if any(len(e) is not len(matrix[0]) for e in matrix):
        raise TypeError("Each row of the matrix must have the same size")
