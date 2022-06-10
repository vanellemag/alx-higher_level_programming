#!/usr/bin/python3
def square(x):
    return(x**2)


def square_matrix_simple(matrix=[]):
    new = []
    for i in range(len(matrix)):
        new.append(list(map(square, matrix[i])))
    return(new)
