from __future__ import division
import math
from approximation.algebraic import calculate_algebraic, algebraic_approximation
from approximation.trigonometric import trigonometric_approximation, calculate_trigonometric
from interpolation.newton_lagrange import generate_points_for_function
import matplotlib.pyplot as plt

__author__ = 'Joanna Sendorek'


def function(x):
    return math.exp(2.0 * math.cos(x))

if __name__ == '__main__':

        for j in [10, 15, 20, 30, 40, 50, 100, 200, 500, 1000]:
            for i in range(int(j/20), min(101, int((j-1)/2)), max(1, int(j/20))):

                n = j  # points number
                m = i  # polynomial degree

                start = -2.0 * math.pi
                end = math.pi * 4.0
                step = (end - start)/1000
                points, values = generate_points_for_function(start, end, function, n)

                # for plots
                pnts = []
                trigonometric = []
                for_errs_trigs = []

                reals = []
                for_errs_reals = []

                algebraics = []
                for_errs_algebraics = []

                temp = start - 1
                trigonometric_polynomial = trigonometric_approximation(n, m, points, values)
                algebraic_polynomial = algebraic_approximation(n, m, points, values)

                while temp < end + 1:

                    pnts.append(temp)

                    trigonometric_value = calculate_trigonometric(temp, trigonometric_polynomial, m)
                    algebraic_value = calculate_algebraic(temp, algebraic_polynomial, m)
                    real_value = function(temp)

                    if end >= temp >= start:

                        for_errs_reals.append(real_value)
                        for_errs_trigs.append(trigonometric_value)
                        for_errs_algebraics.append(algebraic_value)

                    trigonometric.append(trigonometric_value)
                    reals.append(real_value)
                    algebraics.append(algebraic_value)

                    temp += step

                max_error_trig = max(math.fabs((for_errs_trigs[j] - for_errs_reals[j])) for j in
                                     range(len(for_errs_reals)))

                error_trig = math.sqrt(sum(math.pow((for_errs_trigs[j] - for_errs_reals[j]), 2)
                                       for j in range(len(for_errs_reals))) / len(for_errs_reals))

                max_error_algebraic = max(math.fabs((for_errs_algebraics[j] - for_errs_reals[j])) for j in
                                          range(len(for_errs_reals)))

                error_algebraic = math.sqrt(sum(math.pow((for_errs_algebraics[j] - for_errs_reals[j]), 2)
                                            for j in range(len(for_errs_reals))) / len(for_errs_reals))

                print(str(m) + ", " + str(n) + ", " + str(max_error_trig) + ", " + str(error_trig) + ", " +
                      str(max_error_algebraic) + ", " + str(error_algebraic))

                plt.plot(pnts, trigonometric, 'r-', label="trigonometric")
                plt.plot(pnts, algebraics, 'm-', label="algebraic")
                plt.plot(pnts, reals, 'b-', label="function")
                plt.axhline(0, color='black', linestyle='dashdot')

                plt.axis([start-1, end+1, min([min(for_errs_algebraics), min(for_errs_trigs), min(for_errs_reals)]) - 1,
                          max([max(for_errs_reals), max(for_errs_trigs), min(for_errs_algebraics)]) + 1])
                plt.plot(points, [function(point) for point in points], 'ro')
                legend = plt.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc=3, ncol=3, mode="expand", borderaxespad=0.)
                for label in legend.get_texts():
                    label.set_fontsize(10)
                file_name = '../plots/approx/' + "degree" + str(m) + "points" + str(n) + '.png'
                plt.savefig(file_name)
                plt.close()
                # plt.show()