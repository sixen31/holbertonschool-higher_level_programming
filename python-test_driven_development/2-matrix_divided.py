#!/usr/bin/python3


def matrix_divided(matrix, div):
    new_matrix = []
    for row in matrix:
        new_row = []
        for num in row:
            new_num = round(num / div, 2)
            new_row.append(new_num)
        new_matrix.append(new_row)
    return new_matrix
