from matrix.matrix_operations import create_vector, count_system_error, create_matrix, reverse_matrix, maximum_norm

__author__ = 'Joanna Sendorek'

MAX_STEPS = 1000


def jacobie_method(matrix, vector, precision, norm, n):
    # norm can be maximum or euclidean
    x_error = create_vector(n)
    x = create_vector(n)

    for i in range(n):
        x[i] = 0

    for i in range(n):
        vector[i] = vector[i] / matrix[i][i]

        for j in range(n):
            if i == j:
                continue
            matrix[i][j] /= matrix[i][i]
            x_error[i] = float("inf")

    steps = 0

    # while norm(x_error) > precision and steps < MAX_STEPS:
    while norm(count_system_error(matrix, x, vector, n)) > precision and steps < MAX_STEPS:
        print(norm(count_system_error(matrix, x, vector, n)))
        steps += 1
        for i in range(n):
            temp = vector[i]
            for j in range(n):
                if i == j:
                    continue
                temp -= matrix[i][j] * x[j]

            x_error[i] = x[i] - temp
            x[i] = temp

    print("steps: " + str(steps))
    return x


def SOR(matrix, B, omega, n, eps):
    x_error = create_vector(n)
    x = create_vector(n)
    temp2 = create_vector(n)

    iteration = create_matrix(n)
    temp = create_matrix(n)

    for i in range(n):
        for j in range(n):
            if j > i:
                iteration[i][j] = 0
            elif j == i:
                iteration[i][j] = (1.0/omega) * matrix[i][j]
            else:
                iteration[i][j] = (-1) * matrix[i][j]
    iteration = reverse_matrix(iteration, n)

    for i in range(n):
        for j in range(n):
            temp[i][j] = 0
            for k in range(n):
                temp[i][j] += iteration[i][k] * matrix[k][j]

    for i in range(n):
        temp2[i] = 0
        for j in range(n):
            temp2[i] += iteration[i][j] * B[j]

    for i in range(n):
        for j in range(n):
            if i == j:
                iteration[i][j] = 1 - temp[i][j]
            else:
                iteration[i][j] = (-1) * temp[i][j]
        B[i] = temp2[i]

    for i in range(n):
        x_error[i] = 1e+300
        x[i] = 1

    epsilon = eps
    steps = 0

    while maximum_norm(x_error) > epsilon and steps < MAX_STEPS:
        steps += 1
        for i in range(n):
            for j in range(n):
                temp3 = 0
                for k in range(n):
                    temp3 += iteration[j][k] * x[k]
                temp3 += B[j]
                x_error[j] = x[j] - temp3
                x[j] = temp3

    # print("steps:" + str(steps))
    return x, steps