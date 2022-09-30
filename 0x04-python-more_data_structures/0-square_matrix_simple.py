#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    x = []
    for x in matrix:
        x.append(list(map(lambda x: x**2, x)))
    return (x)
