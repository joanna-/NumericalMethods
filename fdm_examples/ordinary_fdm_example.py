from __future__ import division
import math
import matplotlib.pyplot as plt
from differentials.euler_kutta import constant_points
from linear_equations.direct_methods import thomas_algorithm
from matrix.matrix_operations import create_tridiagonal


__author__ = 'Joanna Sendorek'

k = 1
m = 2


def fdm(a, b, n):
    x, h = constant_points(a, b, n)
    matrix = create_tridiagonal(n)

    y = [0 for i in range(n)]

    for i in range(n):
        y[i] = math.pow(m, 2) * math.pow(h, 2)*k*x[i]
        matrix[i][0] = 1
        matrix[i][1] = math.pow(m, 2) * math.pow(h, 2) - 2
        matrix[i][2] = 1

    matrix[0][0] = 0
    matrix[0][1] = 1
    matrix[0][2] = 0

    matrix[n-1][0] = 0
    matrix[n-1][1] = 1
    matrix[n-1][2] = 0

    y[0] = 0
    y[n-1] = calculate_solution(b)

    matrix, y = thomas_algorithm(matrix, y, n)
    max_error = 0
    for i in range(n):
        temp = calculate_solution(x[i])
        if abs(y[i]-temp) > max_error:
            max_error = abs(y[i] - temp)

    return x, y, max_error


def calculate_solution(x):
    return -k*math.sin(m*x) + k*x

if __name__ == '__main__':
    for point in [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 30, 40, 50, 60, 70, 80, 90, 100,
                  500, 1000, 5000, 10000, 50000, 100000, 500000]:
        point += 1
        a = 0
        b = (2*math.pi + 1) * 0.5

        x = []
        exacts = []

        points, solutions, max_error = fdm(a, b, point)

        error = ""
        error += str(point-1) + ", "
        error += str(max_error) + ", "
        print(error)

        step = (b-a)/499
        for i in range(500):
            x.append(a+i*step)
            exacts.append(calculate_solution(a+i*step))

        plt.figure(0)
        plt.plot(x, exacts, 'r-', label="function")
        plt.plot(points, solutions, 'b-', label="fdm_examples")
        if point < 11:
            plt.plot(points, solutions, 'go')

        # plt.axis([a-1, b+1, -1.0, 50.0])

        legend = plt.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc=3, ncol=3, mode="expand", borderaxespad=0.)
        for label in legend.get_texts():
            label.set_fontsize(10)
        file_name = '../plots/diff/fdm' + str(point) + '.png'
        plt.savefig(file_name)
        plt.close()

