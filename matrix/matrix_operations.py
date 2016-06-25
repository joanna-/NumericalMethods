from __future__ import division
import math


__author__ = 'Joanna Sendorek'


def create_unit_matrix(n):
    matrix = create_matrix(n)
    for i in range(n):
        matrix[i][i] = 1.0
    return matrix


def create_matrix(rows, cols=None):
    if cols is None:
        return [[0 for x in range(rows)] for x in range(rows)]
    return [[0 for j in range(cols)] for i in range(rows)]


def create_tridiagonal(size):
    return [[0 for i in range(3)] for j in range(size)]


def multiply_matrixes(matrix_1, matrix_2, result, rows, cols):
    for i in range(cols+1):
        for j in range(cols+1):
            result[i][j] = 0
            for k in range(rows):
                result[i][j] += matrix_2[i][k] * matrix_1[k][j]
    return result


def multiply_vector(matrix, result, rows, cols, values):

    for i in range(cols):
        result[i] = 0
        for j in range(rows):
            result[i] += \
                matrix[i][j] \
                * values[j]
    return result


def create_vector(n):
    return [0 for x in range(n)]


def print_matrix(matrix, n):
    for i in range(n):
        row = ""
        for j in range(n):
            row += '\t' + str(matrix[i][j])
        print(row + '\n')


def print_vector(vector, n):
    for i in range(n):
        print(vector[i])


def euclidean_norm(vector):
    return math.sqrt(math.fsum(el * el for el in vector))


def maximum_norm(vector):
    return max(math.fabs(el) for el in vector)


def vector_of_errors(vector1, vector2):
    return [math.fabs((vector1(i) - vector2(i))/vector2(i)) for i in len(vector1)]


def vector_difference(vector1, vector2):
    return [vector1[i] - vector2[i] for i in range(len(vector1))]


def reverse_matrix(matrix, n):
    reverse = [[1 if x == y else 0 for x in range(n)] for y in range(n)]

    for i in range(n):
        divisor = matrix[i][i]
        for j in range(i, n):
            matrix[i][j] /= divisor
        for j in range(n):
            reverse[i][j] /= divisor

        for j in range(i+1, n):
            factor = matrix[i][j]
            for k in range(i, n):
                matrix[j][k] -= factor * matrix[i][k]
            for k in range(n):
                reverse[j][k] -= factor * reverse[i][k]

    for i in range(n-1, -1, -1):
        for j in range(i-1, -1, -1):
            factor = matrix[i][j]
            matrix[j][i] = 0
            for k in range(n):
                reverse[j][k] -= factor * reverse[i][k]

    return reverse


def matrix_condition(matrix, n):
    return matrix_norm(matrix, n) * matrix_norm(reverse_matrix(matrix, n), n)


def matrix_norm(matrix, n):
    return max(sum(math.fabs(el) for el in matrix[i]) for i in range(n))


def calculate_constant_terms_vector(matrix, vector_x, n):
    vector_b = create_vector(n)
    for i in range(n):
        vector_b[i] = sum(matrix[i][j] * vector_x[j] for j in range(n))
    return vector_b


def count_system_error(matrix, vector_x, vector_b, n):
    output = create_vector(n)
    for i in range(n):
        for j in range(n):
            if i == j:
                output[i] += matrix[i][j] * vector_x[j]
            else:
                output[i] += matrix[i][j] * matrix[i][i] * vector_x[j]
        output[i] -= vector_b[i] * matrix[i][i]
    return output


def spectral_radius(matrix, n):
    matrix_copy = create_matrix(n)
    unit_m = create_unit_matrix(n)
    for i in range(n):
        for j in range(n):
            matrix_copy[i][j] += matrix[i][j] / matrix[i][i]
    for i in range(n):
        for j in range(n):
            matrix[i][j] = unit_m[i][j] - matrix_copy[i][j]

    vector_x = create_vector(n)
    temp = create_vector(n)
    for i in range(n):
        vector_x[i] = 1

    steps = 0
    while steps < 50:
        steps += 1
        for i in range(n):
            temp[i] = 0
            for j in range(n):
                temp[i] += matrix[i][j] * vector_x[j]

        norm = euclidean_norm(temp)
        for i in range(n):
            vector_x[i] = temp[i] / norm

    for i in range(n):
        temp[i] = 0
        for j in range(n):
            temp[i] += matrix[i][j] * vector_x[j]

    axx = 0
    for i in range(n):
        axx += temp[i] * vector_x[i]

    xx = 0
    for i in range(n):
        xx += vector_x[i] * vector_x[i]

    return math.fabs(axx/xx)







