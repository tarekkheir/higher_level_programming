#!/usr/bin/python3
"""
Module - matrix divided
Method: matrix_divided
Attribute: matrix, div
"""

def matrix_divided(matrix, div):
    """
    Return matrix divided by div
    """
    if matrix is None:
        return None
    
    new_matrix = []
    if type(matrix) == list:
        for x in matrix:
            if len(x) != len(matrix[0]):
                raise TypeError("Each row of the matrix must have the same size")
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if type(matrix[i][j]) not in [int, float]:
                    raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    if not type(div) in [int, float]:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    for i in range(0, len(matrix)):
        new_matrix.append([])
        for j in range(0, len(matrix[i])):
            add =  round((matrix[i][j] / div), 2)
            new_matrix[i].append(add)

    return new_matrix

