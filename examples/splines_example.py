from __future__ import division
import math
from interpolation.newton_lagrange import generate_points_for_function
from splines.cubic import cubic_spline
from splines.squares import square_spline
import matplotlib.pyplot as plt

__author__ = 'Joanna Sendorek'


def value_for_spline(x, points, n, splines, start):
    distance = points[1] - points[0]
    spline_number = int((x - start) / distance)

    while spline_number > n - 2:
        spline_number -= 1

    return splines[spline_number].calculate_value(x - points[spline_number])


def function(x):
    return math.exp(2.0 * math.cos(x))


if __name__ == '__main__':
    for i in list(range(4, 31)) + list(range(35, 80, 5)):
        start = -2.0 * math.pi
        end = math.pi * 4.0
        step = (end-start)/1000
        points, values = generate_points_for_function(start, end, function, i)

        cubic_splines = cubic_spline(points, values, i, 'natural')
        square_splines = square_spline(points, values, i, 'natural')

        # for plots
        pnts = []
        cubics = []
        reals = []
        squares = []

        for_errs_cubics= []
        for_errs_squares= []
        for_errs_reals= []

        temp = start

        while temp <= end:

            pnts.append(temp)

            cubic_value = value_for_spline(temp, points, i, cubic_splines, start)
            square_value = value_for_spline(temp, points, i, square_splines, start)
            real_value = function(temp)

            for_errs_cubics.append(cubic_value)
            for_errs_squares.append(square_value)
            for_errs_reals.append(real_value)

            cubics.append(cubic_value)
            squares.append(square_value)
            reals.append(real_value)

            temp += step

        max_error_square = max(math.fabs((for_errs_squares[j] - for_errs_reals[j])) for j in range(len(for_errs_reals)))
        max_error_cubic = max(math.fabs((for_errs_cubics[j] - for_errs_reals[j])) for j in range(len(for_errs_reals)))

        error_square = math.sqrt(sum(math.pow((for_errs_squares[j] - for_errs_reals[j]), 2)
                                 for j in range(len(for_errs_reals))) / len(for_errs_reals))
        error_cubic = math.sqrt(sum(math.pow((for_errs_cubics[j] - for_errs_reals[j]), 2)
                                for j in range(len(for_errs_reals))) / len(for_errs_reals))

        print(str(i) + ", " + str(max_error_cubic) + ", " + str(max_error_square) + ", " + str(error_cubic)
              + ", " + str(error_square))

        plt.figure(i)
        plt.plot(pnts, reals, 'r-', label="function")
        plt.plot(pnts, cubics, 'g-', label="cubic splines")
        plt.plot(pnts, squares, 'b-', label="square splines")
        plt.axhline(0, color='black', linestyle='dashdot')

        plt.axis([start-1, end+1, min(for_errs_squares + for_errs_cubics + for_errs_reals)-1,
                  max(for_errs_squares + for_errs_cubics + for_errs_reals)+1])
        plt.plot(points, [function(point) for point in points], 'ro')
        legend = plt.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc=3, ncol=3, mode="expand", borderaxespad=0.)
        for label in legend.get_texts():
            label.set_fontsize(10)
        file_name = '../plots/splines/v1' + str(i) + '.png'
        plt.savefig(file_name)
        plt.close()
        # plt.show()


