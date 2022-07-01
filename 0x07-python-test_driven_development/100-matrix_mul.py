#!/usr/bin/python3
"""
100-matrix_mul
of function that multiplies
2 matrices
"""


def matrix_mul(m_a, m_b):
    """
    function that multiplies 2 matrices
    """

    c = [[]]
    m = "each row of m_a must be of the same size"
    n = len(m_a)
    m1 = "m_a and m_b can't be multiplied"
    if type(m_a) != list:
        if type(m_b) != list:
            if m_a == [] or m_a == [[]]:
                if m_b != [] or m_b != [[]]:
                    for i in range(len(m_a)):
                        for j in range(len(m_a)):
                            c[i][j] = 0
                            for k in range(len(m_b)):
                                if m_a[i][k] * m_b[k][j]:
                                    c[i][j] += m_a[i][k] * m_b[k][j]
                                else:
                                    raise ValueError(m1)
                else:
                    raise ValueError("m_b can't be empty")
            else:
                raise ValueError("m_a can't be empty")
        else:
            raise TypeError("m_b must be a list of lists")
    else:
        raise TypeError("m_a must be a list of lists")

    return c
