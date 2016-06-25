from __future__ import division
import math
from interpolation.hermite import calculate_hermite
from interpolation.newton_lagrange import newton_polynomial, lagrange_polynomial, generate_points_for_function
import matplotlib.pyplot as plt

__author__ = 'Joanna Sendorek'


def derivative(x):
    return -2 * math.sin(x) * math.exp(2*math.cos(x))


def function(x):
    return math.exp(2.0 * math.cos(x))

if __name__ == '__main__':
    for i in list(range(2, 31)) + list(range(35, 80, 5)):
        start = -2.0 * math.pi
        end = math.pi * 4.0
        step = (end-start)/1000
        points, values = generate_points_for_function(start, end, function, i)

        # for plots
        pnts = []
        newtons = []
        reals = []
        lagranges = []
        hermites = []

        for_errs_lagranges= []
        for_errs_newtons=[]
        for_errs_reals=[]
        for_errs_hermites = []

        temp = start-1

        while temp < end+1:

            pnts.append(temp)

            newton_value = newton_polynomial(temp, i, points, values)
            lagrange_value = lagrange_polynomial(temp, i, points, values)
            real_value = function(temp)
            hermite_value = calculate_hermite(temp, i, points, values, derivative)

            if end >= temp >= start:
                for_errs_lagranges.append(lagrange_value)
                for_errs_newtons.append(newton_value)
                for_errs_reals.append(real_value)
                for_errs_hermites.append(hermite_value)

            newtons.append(newton_value)
            lagranges.append(lagrange_value)
            reals.append(real_value)
            hermites.append(hermite_value)

            temp += step

        max_error_lagrange = max(math.fabs((for_errs_lagranges[j] - for_errs_reals[j])) for j in range(len(for_errs_reals)))
        max_error_newton = max(math.fabs((for_errs_newtons[j] - for_errs_reals[j])) for j in range(len(for_errs_reals)))
        max_error_hermite = max(math.fabs((for_errs_hermites[j] - for_errs_reals[j])) for j in range(len(for_errs_reals)))

        error_lagrange = math.sqrt(sum(math.pow((for_errs_lagranges[j] - for_errs_reals[j]), 2)
                                       for j in range(len(for_errs_reals))) / len(for_errs_reals))
        error_newton = math.sqrt(sum(math.pow((for_errs_newtons[j] - for_errs_reals[j]), 2)
                                     for j in range(len(for_errs_reals))) / len(for_errs_reals))
        error_hermite = math.sqrt(sum(math.pow((for_errs_hermites[j] - for_errs_reals[j]), 2)
                                      for j in range(len(for_errs_reals))) / len(for_errs_reals))

        print("number of points: " + str(i))
        print("maximum error lagrange: " + str(max_error_lagrange))
        print("maximum error newton: " + str(max_error_newton))
        print("maximum error hermite: " + str(max_error_hermite))
        print("error lagrange: " + str(error_lagrange))
        print("error newton: " + str(error_newton))
        print("error hermite: " + str(error_hermite))

        plt.figure(i)
        plt.plot(pnts, reals, 'r-', label="function")
        plt.plot(pnts, newtons, 'g-', label="newton polynomial")
        plt.plot(pnts, lagranges, 'b-', label="lagrange polynomial")
        plt.plot(pnts, hermites, 'm-', label="hermite polynomial")
        plt.axhline(0, color='black', linestyle='dashdot')

        plt.axis([start-1, end+1, -10.0, 10.0])
        plt.plot(points, [function(point) for point in points], 'ro')
        legend = plt.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc=3, ncol=3, mode="expand", borderaxespad=0.)
        for label in legend.get_texts():
            label.set_fontsize(10)
        file_name = '../plots/hermiteR' + str(i) + '.png'
        plt.savefig(file_name)
        plt.close()
        # plt.show()

