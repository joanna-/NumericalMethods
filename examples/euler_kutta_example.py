import math
import matplotlib.pyplot as plt
from differentials.euler_kutta import general_method, calculate_euler, calculate_Runge_Kutta

__author__ = 'Joanna Sendorek'


def calculate_equation(x, y):
    return 4*math.sin(x)*math.cos(x)+2*y*math.sin(x)


def calculate_solution(x):
    return math.exp((-2.0)*math.cos(x)) - 2.0*math.cos(x) + 1.0


if __name__ == '__main__':
    for point in [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 150, 250, 500, 750, 1000, 2500, 5000, 10000]:
        point += 1
        a = math.pi * 0.5
        b = math.pi * 3.5

        x = []
        exacts = []

        error = ""

        points, solutions, max_err_euler = general_method(a, b, point, calculate_euler, calculate_solution)
        points_k, solutions_kutta, max_err_kutta = general_method(a, b, point, calculate_Runge_Kutta,
                                                                  calculate_solution)

        error = ""
        error += str(point) + ", "
        error += str(max_err_euler) + ", "
        error += str(max_err_kutta)
        print(error)

        step = (b-a)/499
        for i in range(500):
            x.append(a+i*step)
            exacts.append(calculate_solution(a+i*step))

        plt.figure(point)
        plt.plot(x, exacts, 'r-', label="function")
        plt.plot(points, solutions, 'b-', label="Euler")
        plt.plot(points_k, solutions_kutta, 'm-', label="Kutta")
        if point < 500:
            plt.plot(points, solutions, 'bo')
            plt.plot(points_k, solutions_kutta, 'mo')
        plt.axhline(0, color='black', linestyle='dashdot')

        legend = plt.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc=3, ncol=3, mode="expand", borderaxespad=0.)
        for label in legend.get_texts():
            label.set_fontsize(10)
        file_name = '../plots/diff/diffs' + str(point) + '.png'
        plt.savefig(file_name)
        plt.close()
