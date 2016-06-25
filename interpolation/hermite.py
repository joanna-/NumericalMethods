from matrix.matrix_operations import create_matrix

__author__ = 'Joanna Sendorek'


def fill_hermite_differences(n, points, values, derivative):
    differences = create_matrix(2*n+1)
    for i in range(0, 2*n, 2):
        differences[i][0] = points[int(i/2)]
        differences[i+1][0] = points[int(i/2)]
        differences[i][1] = values[int(i/2)]
        differences[i+1][1] = values[int(i/2)]

    for i in range(2, 2*n+1):
        for j in range(1+(i-2), 2*n):
            if i == 2 and j % 2 == 1:
                differences[j][i] = derivative(points[int(j/2)])
            else:
                differences[j][i] = (differences[j][i-1] - differences[j-1][i-1]) / \
                                    (differences[j][0] - differences[(j-1)-(i-2)][0])
    return differences


def calculate_hermite(x, n, points, values, derivative):
    differences = fill_hermite_differences(n, points, values, derivative)
    result = 0
    for i in range(2*n):
        factor = 1
        j = 0
        while j < i:
            factor *= (x - points[int(j/2)])
            if j+1 != i:
                factor *= (x - points[int(j/2)])
                j += 1
            j += 1

        result += factor * differences[i][i+1]

    return result



