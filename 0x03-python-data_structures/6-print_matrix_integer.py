#!/usr/bin/python3


def print_matrix_integer(matrix=[[]]):
    for line in range(len(matrix)):
        for col in range(len(matrix[line])):
            print("{:d}".format(matrix[line][col]), end=" ")
            if col != len(matrix[line]) - 1:
                print("{}".format(""), end=" ")
        print()
