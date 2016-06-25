from __future__ import division
import math

__author__ = 'Joanna Sendorek'

MAX_STEPS = 100000
epsilon = 1e-10     # for criteria to when we will do all calculations


def newton_algorithm(start_point, function, derivative):
    steps = 0
    current_x = start_point
    previous_x = float('inf')

    while math.fabs(current_x - previous_x) > epsilon and steps < MAX_STEPS:
        try:
            while math.fabs(function(current_x)) > epsilon and steps < MAX_STEPS:
                steps += 1
                previous_x = current_x
                try:
                    current_x = previous_x - ((function(previous_x))/(derivative(previous_x)))
                except OverflowError:
                    print("OVERFLOW")
                    print("Steps:" + str(steps))
                    print("CurrentX: " + str(current_x))
                    print("PreviousX: " + str(previous_x))
                    print("\n")
                    return
        except OverflowError:
            print("OVERFLOW")
            print("Steps:" + str(steps))
            print("CurrentX: " + str(current_x))
            print("PreviousX: " + str(previous_x))
            print("\n")
            return

    print("Steps: " + str(steps))

    return current_x


def secant_method(start_point, end_point, function):
    steps = 0

    current_x = start_point
    previous_x = end_point

    current_y = function(current_x)
    previous_y = function(previous_x)

    while math.fabs(current_x - previous_x) > epsilon and steps < MAX_STEPS:
    # while math.fabs(function(current_x)) > epsilon and steps < MAX_STEPS:
        steps += 1

        if math.fabs(previous_y) < math.fabs(current_y):
            current_y, previous_y = previous_y, current_y
            current_x, previous_x = previous_x, current_x

        try:
            temp = (previous_x - current_x)/(previous_y - current_y)
        except ZeroDivisionError:
            print("ZERO DIVISION")
            print("Steps:" + str(steps))
            print("CurrentX: " + str(current_x))
            print("CurrentY: " + str(current_y))
            print("PreviousX: " + str(previous_x))
            print("PreviousY: " + str(previous_y))
            print("\n")
            return
        previous_x = current_x
        previous_y = current_y

        current_x = current_x - (current_y * temp)
        try:
            current_y = function(current_x)
        except OverflowError:
            print("CurrentX: " + str(current_x))
            print("CurrentY: " + str(current_y))
            print("PreviousX: " + str(previous_x))
            print("PreviousY: " + str(previous_y))
            print("OVERFLOW")
            print("Steps:" + str(steps))
            print("CurrentX: " + str(current_x))
            print("\n")
            return

    print("Steps: " + str(steps))
    return current_x


