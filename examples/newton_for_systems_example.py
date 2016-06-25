from matrix.matrix_operations import print_vector, create_matrix, create_vector
from nonlinear_equations.newton_for_systems import calculate_system

__author__ = 'Joanna Sendorek'


def function_for_solution(solution, n):
    x = solution[0]
    y = solution[1]
    z = solution[2]
    function = create_vector(n)

    function[0] = (x*x + y*y - z*z - 1) * (-1)
    function[1] = (x - 2*y*y*y + 2*z*z + 1) * (-1)
    function[2] = (2*x*x + y - 2*z*z - 1) * (-1)

    return function


def derivative_for_solution(solution, n):
    x = solution[0]
    y = solution[1]
    z = solution[2]
    derivative = create_matrix(n)

    derivative[0][0] = 2*x
    derivative[0][1] = 2*y
    derivative[0][2] = -2*z

    derivative[1][0] = 1
    derivative[1][1] = (-6)*y*y
    derivative[1][2] = 4*z

    derivative[2][0] = 4*x
    derivative[2][1] = 1
    derivative[2][2] = -4*z

    return derivative

if __name__ == "__main__":
    vectors = [[1000, 1000, 1000], [-1000, 1000, -1000], [1, 1000, -1], [-1, 1000, 1],
               [-1000, -1000, -1000], [1000, -1000, 1000], [1000, 1, 1000], [1, 1, 1],
               [-1, -1, -1], [1, -1, 1], [1000, 1, -1000], [-1000, 1, -1000],
               [1000, 1000, -1000], [-1000, 1, 1], [-1, 1000, -1], [1, 1, -1], [-1000, 1000, 1000],
               [1, 1000, 1], [-1000, 1, -1], [-1000, 1, 1000]]

    for vector in vectors:
        print_vector(vector, 3)
        result = calculate_system(3, vector,function_for_solution, derivative_for_solution)
        if result is not None:
            print("Steps: " + str(result[0]))
            print("Solution: " + str(result[1]))
            print("\n")