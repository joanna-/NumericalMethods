from __future__ import division
from abc import ABCMeta, abstractmethod

__author__ = 'Joanna Sendorek'


class Polynomial:

    __metaclass__ = ABCMeta

    def __init__(self, grade):
        self.grade = grade

    @abstractmethod
    def calculate_value(self, x):
        pass


class SquarePolynomial(Polynomial):
    grade = 2

    def __init__(self, a, b, c):
        super(SquarePolynomial, self).__init__(2)
        self.a = a
        self.b = b
        self.c = c

    def calculate_value(self, x):
        return self.a * x * x + self.b * x + self.c


class CubicPolynomial(Polynomial):

    def __init__(self, a, b, c, d):
        super(CubicPolynomial, self).__init__(2)
        self.a = a
        self.b = b
        self.c = c
        self.d = d

    def calculate_value(self, x):
        return self.a * x * x * x + self.b * x * x + self.c * x + self.d

    def __str__(self):
        return str(self.a) + ", " + str(self.b) + ", " + str(self.c) + ", " + str(self.d)