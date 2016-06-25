import math
from matrix.matrix_operations import create_vector

__author__ = "Joanna Sendorek"


def trigonometric_approximation(n, m, points, values):
    vals = create_vector(2*m+1)
    vals[0] = 0
    for i in range(n):
        vals[0] += values[i]

    vals[0] *= 2.0/n

    for k in range(1, m+1, 1):
        a = 0
        for i in range(n):
            a += values[i] * math.cos(k*((2*math.pi)/(6*math.pi)) * points[i])
        a *= 2.0 / n

        b = 0
        for i in range(n):
            b += values[i] * math.sin(k*((2*math.pi)/(6*math.pi)) * points[i])
        b *= 2.0 / n

        vals[2*k - 1] = a
        vals[2*k] = b

    return vals


def calculate_trigonometric(x, polynomial, m):
    result = polynomial[0]/2
    factor = x

    for i in range(1, 2*m, 2):
        result += polynomial[i] * math.cos(((2*math.pi)/(6*math.pi)) * factor)
        result += polynomial[i+1] * math.sin(((2*math.pi)/(6*math.pi)) * factor)
        factor += x
    return result