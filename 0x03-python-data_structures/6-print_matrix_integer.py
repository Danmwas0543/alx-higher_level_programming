#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix:
        for j in matrix:
            for k in j:
                print("".format(k), end=' ' if k != j[-1] else '')
            print()
