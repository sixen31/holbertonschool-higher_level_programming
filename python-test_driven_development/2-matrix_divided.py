#!/usr/bin/python3
"""define class"""


def matrix_divided(matrix, div):
    """Divides all elements in a matrix by a given divisor."""
    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number (integer or float)")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = []
    for row in matrix:
        new_row = []
        for num in row:
            new_num = round(num / div, 2)
            new_row.append(new_num)
        new_matrix.append(new_row)
    return new_matrix
