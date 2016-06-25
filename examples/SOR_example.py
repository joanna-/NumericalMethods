from examples.jacobie_example import fill_matrix
from linear_equations.indirect_methods import SOR
from matrix.matrix_operations import create_matrix, create_vector, calculate_constant_terms_vector, euclidean_norm, \
    maximum_norm, vector_difference

__author__ = 'Joanna Sendorek'


def f1(vector, n):
    for i in range(n):
        if i % 2 == 0:
            vector[i] = -1
        else:
            vector[i] = 1


def f2(vector, n):
    for i in range(n):
        if i % 2 == 0:
            vector[i] = 1
        else:
            vector[i] = -1


def f3(vector, n):
    for i in range(n):
        vector[i] = 1000


def f4(vector, n):
    for i in range(n):
        vector[i] = 1


def f5(vector, n):
    for i in range(n):
        vector[i] = 0


def f6(vector, n):
    for i in range(n):
        vector[i] = -1000


def f7(vector, n):
    for i in range(n):
        if i % 2 == 0:
            vector[i] = 1000
        else:
            vector[i] = -1000


def f8(vector, n):
    for i in range(n):
        if i % 2 == 0:
            vector[i] = -1000
        else:
            vector[i] = 1000


def f9(vector, n):
    for i in range(n):
        if i % 2 == 0:
            vector[i] = 1000
        else:
            vector[i] = 0


def f10(vector, n):
    for i in range(n):
        if i % 2 == 0:
            vector[i] = 0
        else:
            vector[i] = 1

if __name__ == "__main__":
    for i in [1e-10]:
        k = 10
        matrix_A = create_matrix(k)
        fill_matrix(matrix_A, k)

        vector_X = create_vector(k)

        for func in [f1, f2, f3, f4, f5, f6, f7, f8, f9, f10]:
            func(vector_X, k)
            vector_B = calculate_constant_terms_vector(matrix_A, vector_X, k)

            x, it = SOR(matrix_A, vector_B, 0.1, k, i)
            euclidean = euclidean_norm(vector_difference(vector_X, x))
            maximum = maximum_norm(vector_difference(vector_X, x))
            print(str(it) + ", " + str(euclidean) + ", " + str(maximum))