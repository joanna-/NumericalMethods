from __future__ import division
from linear_equations.direct_methods import gaussian_elimination
from matrix.matrix_operations import create_vector, maximum_norm


MAX_STEPS = 1000

def calculate_solution(vector, n):
    x = vector[0]
    y = vector[1]
    z = vector[2]

    result = create_vector(n)

    result[0] = x*x + y*y - z*z - 1
    result[1] = x - 2*y*y*y + 2*z*z + 1
    result[2] = 2*x*x + y - 2*z*z - 1

    return result


def calculate_system(n,  initial_vector, function_for_solution, derivative_for_solution):
    epsilon = 1e-10
    steps = 0

    solution = initial_vector
    previous = create_vector(n)
    for i in range(n):
        previous[i] = initial_vector[i]

    # while (steps == 0) or (maximum_norm(vector_difference(solution, previous)) > epsilon and steps < MAX_STEPS):
    while maximum_norm(calculate_solution(solution, n)) > epsilon and steps < MAX_STEPS:
        steps += 1

        function = function_for_solution(solution, n)
        derivative = derivative_for_solution(solution, n)

        for i in range(n):
            previous[i] = solution[i]

        temp = gaussian_elimination(matrix_a=derivative, vector_b=function, n=n)
        if temp is None:
            return
        # print(temp)
        for i in range(n):
            temp[i] += previous[i]
            solution[i] = temp[i]

    # print(previous)
    # print(solution)
    # print(vector_difference(solution, previous))

    return steps, solution
