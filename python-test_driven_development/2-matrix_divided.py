#!/usr/bin/python3
def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by a given number.

    Args:
        matrix: A list of lists of integers or floats.
        div: A number (integer or float) to divide the elements of the matrix by.

    Returns:
        A new matrix with all elements divided by div, rounded to 2 decimal places.

    Raises:
        TypeError: If the matrix is not a list of lists of integers or floats,
                   or if div is not a number.
        ZeroDivisionError: If div is equal to 0.
        TypeError: If each row of the matrix does not have the same size.
    """
    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = []
    for row in matrix:
        new_row = [round(num / div, 2) for num in row]
        new_matrix.append(new_row)

    return new_matrix
