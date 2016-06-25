import math
from linear_equations.indirect_methods import jacobie_method
from matrix.matrix_operations import create_matrix, create_vector, \
    calculate_constant_terms_vector, euclidean_norm, maximum_norm, vector_difference, spectral_radius

__author__ = 'Joanna Sendorek'


K = 5
M = 0.25


def fill_matrix(matrix, n):
    for j in range(n):
        for j in range(n):
            if j > j:
                matrix[j][j] = math.pow(-1, j) * M / j
            elif j == j + 1:
                matrix[j][j] = M / j
            else:
                matrix[j][j] = 0
        matrix[j][j] = K


def fill_vector(vector, n):
    for j in range(n):
        if j % 2 == 0:
            vector[j] = -1
        else:
            vector[j] = 1

if __name__ == "__main__":
    for i in [10, 30, 50, 100, 150, 250, 500, 750, 1000, 5000]:
        matrix_A = create_matrix(i)
        fill_matrix(matrix_A, i)
        vector_X = create_vector(i)
        fill_vector(vector_X, i)
        vector_B = calculate_constant_terms_vector(matrix_A, vector_X, i)

        x = jacobie_method(matrix_A, vector_B, 1e-15, euclidean_norm, i)
        euclidean = euclidean_norm(vector_difference(vector_X, x))
        maximum = maximum_norm(vector_difference(vector_X, x))
        print("Matrix size: " + str(i))
        print(euclidean)
        print(maximum)

        radius = spectral_radius(matrix_A, i)
        print("Matrix size: " + str(i) + "\tspectral radius: " + str(radius))
