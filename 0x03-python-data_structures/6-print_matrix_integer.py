#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for lst in matrix:
        if len(lst) > 0:
            print(f"{lst[0]}", end="")
        for element in lst[1:]:
            print(" {:d}".format(element), end="")
        print("")
