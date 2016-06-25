from __future__ import division
import math
from nonlinear_equations.methods import newton_algorithm, secant_method

__author__ = 'Joanna Sendorek'

N = 9.0
M = 40.0


def function1(x):
    return M * x * math.exp(-M) - M * math.exp(-N * x) + 1.0 / (M * N)


def derivative1(x):
    return M * (N * math.exp(-N * x) + math.exp(-M))


if __name__ == '__main__':
    functions = [function1]
    derivatives = [derivative1]

    # ability to choose different start points for methods
    starts = [-1.0]
    ends = [2.0]

    step = 0.1

    for i in range(len(starts)):
        while starts[i] < ends[i]:
            print("Start: " + str(starts[i]) + " End: " + str(ends[i]))
            print("Newton zero: " + str(newton_algorithm(ends[i], functions[i], derivatives[i])))
            print("Newton zero: " + str(newton_algorithm(starts[i], functions[i], derivatives[i])))
            print("Secants zero: " + str(secant_method(starts[i], ends[i], functions[i])))
            starts[i] += 0.1
            ends[i] -= 0.1
