from __future__ import division
from functools import reduce
import math
from matrix.matrix_operations import create_matrix

__author__ = 'Joanna Sendorek'


def fill_diffs(n, points, values):
    diffs = create_matrix(n+1)
    for i in range(n):
        diffs[i][0] = points[i]
        diffs[i][1] = values[i]
    for i in range(2, n+1):
        for j in range(1+(i-2), n):
            diffs[j][i] = (diffs[j][i-1] - diffs[j-1][i-1]) / (points[j] - points[(j-1) - (i-2)])
    return diffs


def newton_polynomial(x, n, points, values):
    diffs = fill_diffs(n, points, values)
    result = 0

    for i in range(n):
        result += reduce(lambda a, b: a * (x-b), points[:i], 1) * diffs[i][i+1]
    return result


def lagrange_coefficient(x, i, points):
    return reduce(lambda a, b: a * ((x-b)/(points[i]-b)), points[:i] + points[i+1:], 1)


def lagrange_polynomial(x, n, points, values):
    return reduce(lambda a, b: a + values[b] * lagrange_coefficient(x, b, points), range(n), 0)


def generate_points_for_function(start, end, function, n):
    points = [start + i * (end-start)/(n-1) for i in range(n)]
    return points, [function(points[i]) for i in range(n)]


def czebyszew_points(start, end, function, n):
    half_len = (end-start) / 2
    mid = start + half_len
    points = [mid + math.cos((2*i+1) * math.pi/(2*n)) * half_len for i in range(n)]
    return points, [function(points[i]) for i in range(n)]






