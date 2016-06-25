from __future__ import division

__author__ = 'Joanna Sendorek'


def calculate_euler(n, x, y, h, calculate_equation):
    return y[n] + h * calculate_equation(x[n], y[n])


def constant_points(a, b, n):
    h = (b-a)/(n-1)
    x = [0 for i in range(n)]
    for i in range(n):
        x[i] = a + i*h
    return x, h


def calculate_Runge_Kutta(n, x, y, h, calculate_equation):
    k1 = h * calculate_equation(x[n], y[n])
    k2 = h * calculate_equation(x[n] + h/2, y[n] + 0.5*k1)
    k3 = h * calculate_equation(x[n] + h/2, y[n] + 0.5*k2)
    k4 = h * calculate_equation(x[n] + h, y[n] + k3)

    return y[n] + 1/6 * (k1 + 2*k2 + 2*k3 + k4)


def general_method(a, b, n, method, calculate_solution):
    x, h = constant_points(a, b, n)
    y = [0 for i in range(n)]
    y[0] = calculate_solution(a)
    for i in range(1, n):
        y[i] = method(i-1, x, y, h)
    max_error = 0
    for i in range(n):
        temp = calculate_solution(x[i])
        if abs(y[i]-temp) > max_error:
            max_error = abs(y[i] - temp)

    return x, y, max_error