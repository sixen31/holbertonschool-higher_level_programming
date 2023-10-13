#!/usr/bin/python3
"""define class"""


def matrix_divided(matrix, div):
        """Divides all elements in a matrix by a given divisor.

    Args:
        matrix (list of lists): The matrix to be divided.
        div (int or float): The divisor to divide each element in the matrix by.

    Returns:
        list of lists: A new matrix with each element divided by the divisor.
    """
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
