#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    for x in matrix:
        elment = [y**2 for y in x]
        new_matrix.append(elment)
    return new_matrix
