from __future__ import division

import math
from linear_equations.direct_methods import gaussian_elimination
from matrix.matrix_operations import create_vector, create_matrix, multiply_matrixes, multiply_vector

__author__ = "Joanna Sendorek"


def algebraic_approximation(n, m, points, values):
    matrix_a = create_matrix(n, m+1)
    for i in range(n):
        for j in range(m+1):
            matrix_a[i][j] = math.pow(points[i], j)

    matrix_b = create_matrix(m+1, n)
    for i in range(n):
        for j in range(m+1):
            matrix_b[j][i] = matrix_a[i][j]

    coefficients = create_matrix(m+1, m+1)
    coefficients = multiply_matrixes(matrix_a, matrix_b, coefficients, n, m)
    vals = create_vector(m+1)
    vals = multiply_vector(matrix_b, vals, n, m+1, values)
    result = gaussian_elimination(coefficients, vals, m+1)
    return result


def calculate_algebraic(x, polynomial, m):
    power = 1
    result = 0

    for i in range(m+1):
        result += power * polynomial[i]
        power *= x

    return result













