from __future__ import division
import math
from fdm_examples.implicit_fdm_example import fdm_implicit
from matrix.matrix_operations import create_vector, create_matrix
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib import cm


def fdm():
    x_start = 0
    x_end = 2*math.pi
    t_start = 0
    t_end = 3.5
    a = 2

    for pair in [
                (20, 480)
                ]:
        x_points = pair[0] + 1
        t_points = pair[1] + 1

        # vectors created,
        x_step = (x_end - x_start) / (x_points - 1)
        t_step = (t_end - t_start) / (t_points - 1)
        x_coord = create_vector(x_points)

        for i in range(x_points):
            x_coord[i] = x_start + i * x_step

        t_cord = create_vector(t_points)
        for i in range(t_points):
            t_cord[i] = t_start + i * t_step

        # grid created

        meshgrid = create_matrix(t_points, x_points)
        for i in range(x_points):
            meshgrid[0][i] = 2 * math.sin(2*x_coord[i]) * math.exp(-x_coord[i])

        for i in range(t_points):
            meshgrid[i][0] = 0
            meshgrid[i][x_points-1] = 0

        # a*a+k/h*h
        coefficient = (math.pow(a, 2) * t_step) / math.pow(x_step, 2)

        for j in range(1, t_points):
            for i in range(1, x_points-1):
                meshgrid[j][i] = coefficient * meshgrid[j-1][i-1] + \
                             (1-2*coefficient)*meshgrid[j-1][i] + coefficient * meshgrid[j-1][i+1]

        # plot drawing

        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        x = x_coord
        y = t_cord
        X, Y = np.meshgrid(x, y)

        try:
            ax.plot_surface(X, Y, meshgrid, cstride=1, rstride=1, linewidth=0.0, cmap=cm.get_cmap("gist_rainbow"),)

            ax.set_xlabel("os x")
            ax.set_ylabel("os t")
            ax.set_zlabel("rozwiazanie")


            file_name = '../plots/fdm/ex' + str(x_points) + "," + str(t_points) + '.png'
            plt.savefig(file_name)
            # plt.show()
            plt.close()
        except Exception as e:
            print(e.__class__)

        max_val = 0
        for i in range(x_points):
            for j in range(t_points):
                if math.fabs(meshgrid[j][i] > max_val):
                    max_val = abs(meshgrid[j][i])

        print(str(x_points) + ", " + str(t_points) + ", " + str(coefficient) + ", " + str(max_val))

fdm_implicit()
# fdm()






