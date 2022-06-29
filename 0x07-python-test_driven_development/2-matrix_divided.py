#!/usr/bin/python3
"""
2-matrix_divided
module that write function that divides
all element of a matrix
"""


def matrix_divided(matrix, div):
    """
    function that divides all elements of a matrix
    """
    matrix1 = []
    for i in range(len(matrix)):
        matrix1.append(matrix[i])
    try:
        m1 = "Each row of the matrix must have the same size"
        m = "matrix must be a matrix (list of lists) of integers/floats"
        for i in range(len(matrix1)):
            if len(matrix1[i]) == len(matrix1[1]):
                n = len(matrix1[i])
                j = 0
                while j < n:
                    ma = matrix1[i][j]
                    if type(ma) == int or type(ma) == float:
                        if type(div) == int or type(div) == float:
                            if div != 0:
                                ma = matrix1[i][j] / div
                                matrix1[i][j] = round(ma, 2)
                            else:
                                raise ZeroDivisionError("division by zero")
                        else:
                            raise TypeError("div must be a number")
                    else:
                        raise TypeError(m)
                    j = j + 1
            else:
                raise TypeError(m1)
        return matrix1
    except TypeError:
        raise
