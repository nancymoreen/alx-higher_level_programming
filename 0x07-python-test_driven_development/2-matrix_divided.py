#!/usr/bin/python3

def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix.

    Args:
        matrix: List of integers or floats.
        div: Divides all elements of the matrix.

    Raises:
        TypeError: If the matrix is not a list of lists of integers or float.
        TypeError: If rows of the matrix are not of the same size.
        TypeError: If div is not a number(integer or float)
        ZeroDivisionError: If div is equal to 0.

    Returns:
        New matrix
    """

    if div == 0:
        raise ZeroDivisionError("division by zero")
    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix) or \
            not all(isinstance(num, (int, float)) for row in matrix for num in row):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if len(set(len(row) for row in matrix)) > 1:
        raise TypeError("Each row of the matrix must have the saame size")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    new_matrix = [[round(num / div, 2) for num in row] for row in matrix]
    return new_matrix
