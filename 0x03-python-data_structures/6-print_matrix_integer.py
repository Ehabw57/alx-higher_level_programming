#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for list in matrix:
        for elemnt in list:
            print("{:d}".format(elemnt), end=" ")
        print("")
