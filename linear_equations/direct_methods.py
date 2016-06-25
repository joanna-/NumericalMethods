__author__ = 'Joanna Sendorek'


def gaussian_elimination(matrix_a, vector_b, n):
    for i in range(n):
        if matrix_a[i][i] == 0:
            swapped = False
            for j in range(i+1, n):
                if matrix_a[j][i] != 0:
                    for k in range(i, n):
                        matrix_a[i][k], matrix_a[j][k] = matrix_a[j][k], matrix_a[i][k]
                    vector_b[i], vector_b[j] = vector_b[j], vector_b[i]
                swapped = True
                break
            if not swapped:
                print("This system is indeterminate or contradictory")
                continue
        divisor = matrix_a[i][i]
        if divisor == 0:
            print("This system is indeterminate or contradictory")
            continue
        for j in range(i, n):
            matrix_a[i][j] /= divisor
        vector_b[i] /= divisor

        for j in range(i+1, n):
            factor = matrix_a[j][i]
            for k in range(i, n):
                matrix_a[j][k] -= factor * matrix_a[i][k]
            vector_b[j] -= factor * vector_b[i]

    for i in range(n-1, -1, -1):
        for j in range(i-1, -1, -1):
            factor = matrix_a[j][i]
            matrix_a[j][i] = 0
            vector_b[j] -= factor * vector_b[i]
    return vector_b


def thomas_algorithm(matrix, vector, size):
    n = size + 2
    for i in range(size):
        divisor = matrix[i][1]

        for j in range(3):
            matrix[i][j] /= divisor
        vector[i] /= divisor

        if i != size - 1:
            factor = matrix[i+1][0]
            for j in range(2):
                matrix[i+1][j] -= factor * matrix[i][j+1]
            vector[i+1] -= factor * vector[i]

    for i in range(n - 4, -1, -1):
        factor = matrix[i][2]
        matrix[i][2] = 0
        vector[i] -= factor * vector[i+1]

    return matrix, vector