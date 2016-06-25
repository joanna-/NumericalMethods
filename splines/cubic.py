from __future__ import division
from linear_equations.direct_methods import thomas_algorithm
from matrix.matrix_operations import create_vector, create_tridiagonal
from splines.polynomials import CubicPolynomial

__author__ = 'Joanna Sendorek'


def free_column(vector_b, points, values, n):
    factor = 6/((points[1]-points[0])*(points[1]-points[0]))
    for i in range(2, n):
        vector_b[i-2] = values[i] - 2*values[i-1] + values[i-2]
        vector_b[i-2] *= factor

    return vector_b


def create_system_for_cubic(n, variant):
    matrix_a = create_tridiagonal(n-2)
    vector_b = create_vector(n-2)

    for i in range(n-2):
        matrix_a[i][0] = 1
        matrix_a[i][1] = 4
        matrix_a[i][2] = 1

    if n >= 3:
        matrix_a[0][0] = 0
        matrix_a[n-3][2] = 0

        if variant == 'parabolic':
            matrix_a[0][1] = 5
            matrix_a[n-3][1] = 5
    elif variant == 'parabolic':
        matrix_a[0] = 0
        matrix_a[1] = 5
        matrix_a[2] = 0

    return matrix_a, vector_b


def cubic_spline(points, values, n, variant):
    matrix_a, vector_b = create_system_for_cubic(n, variant)

    vector_b = free_column(vector_b, points, values, n)
    matrix_a, vector_b = thomas_algorithm(matrix_a, vector_b, n-2)

    z = create_vector(n)
    for i in range(1, n-1):
        z[i] = vector_b[i-1]

    if variant == 'natural':
        z[0] = 0
        z[n-1] = 0
    elif variant == 'parabolic':
        z[0] = z[1]
        z[n-1] = z[n-2]

    distance = points[1] - points[0]
    splines = []
    for i in range(n-1):
        splines.append(CubicPolynomial((1/(6*distance))*(z[i+1] - z[i]), 0.5 * z[i],
                                       (values[i+1] - values[i])/distance - (distance/6)*(z[i+1] + 2*z[i]), values[i]))

    return splines