#!/usr/bin/python3
"""
The 2-matrix_divided module

This module contains the matrix_divided()
"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by a given divisor.

    Args:
        matrix (list of lists): The matrix to be divided.
        div (int or float): The divisor by which to divide the matrix.

    Returns:
        list of lists: A new matrix with each element divided by div

    Raises:
        TypeError: If matrix is not a list of lists of integers/floats.
                   If each row of the matrix does not have the same size.
                   If div is not a number.
        ZeroDivisionError: If div is equal to 0.
    """
    list_err = "matrix must be a matrix (list of lists) of integers/floats"
    size_err = "Each row of the matrix must have the same size"

    if len(matrix) == 0:
        raise TypeError(list_err)

    if not isinstance(matrix, list):
        raise TypeError(list_err)

    if not all(isinstance(row, list) for row in matrix):
        raise TypeError(list_err)

    if not all(isinstance(elem, (int, float)) for rw in matrix for elem in rw):
        raise TypeError(list_err)

    row_length = len(matrix[0])
    if not all(len(row) == row_length for row in matrix):
        raise TypeError(size_err)

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return ([[round(elem / div, 2) for elem in row] for row in matrix])
