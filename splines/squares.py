import math
from linear_equations.direct_methods import gaussian_elimination
from matrix.matrix_operations import create_matrix, create_vector
from splines.polynomials import SquarePolynomial


__author__ = 'Joanna Sendorek'


def derivative(x):
    return -2 * math.sin(x) * math.exp(2*math.cos(x))


def create_system_for_square(points, values, n, variant):
    matrix_a = create_matrix(3*(n-1))
    vector_b = create_vector(3*(n-1))
    distance = points[1] - points[0]

    for i in range(0, 3*(n-1), 3):
        if i != 3 * (n-2):
            matrix_a[i][i] = 2 * distance
            matrix_a[i][i+1] = 1
            matrix_a[i][i+4] = -1

        else:
            calculate_variant(variant, matrix_a, i, distance)

        j = i + 1
        matrix_a[j][j-1] = distance * distance
        matrix_a[j][j] = distance
        vector_b[j] = values[int(j / 3) + 1] - values[int(j / 3)]

        k = j + 1
        matrix_a[k][k] = 1
        vector_b[k] = values[int(k / 3)]

    return matrix_a, vector_b


def calculate_variant(variant, matrix_a, i, distance):
    if variant == 'natural':
        matrix_a[i][i] = 1
    elif variant == 'derivative':
        matrix_a[i][i] = 2 * distance
        matrix_a[i][i+1] = 1
    return matrix_a


def square_spline(points, values, n, version):
    matrix_a, vector_b = create_system_for_square(points, values, n, version)

    result = gaussian_elimination(matrix_a, vector_b, n=(3*(n-1)))
    splines = []
    for i in range((n-1)):
        splines.append(SquarePolynomial(a=result[3*i], b=result[3*i+1], c=result[3*i+2]))
    return splines
