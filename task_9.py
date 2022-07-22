# Write a function that accepts a square matrix (N x N 2D array) and returns the determinant of the matrix.
# How to take the determinant of a matrix -- it is simplest to start with the smallest cases:
# A 1x1 matrix |a| has determinant = a.
# A 2x2 matrix [ [a, b], [c, d] ] or
# |a  b|
# |c  d|
# has determinant: a*d - b*c.
# The determinant of larger matrices are calculated analogously, e.g. if M is a 4x4 matrix with first row [a, b, c, d], then:
# det(M) = a * det(a_minor) - b * det(b_minor) + c * det(c_minor) - d * det(d_minor)
from copy import deepcopy

import numpy as np

m0 = [[5]]
m1 = [[4, 6], [3, 8]]
m5 = [[2, 4, 2], [3, 1, 1], [1, 2, 0]]


def determinant(matrix):
    return round(np.linalg.det(matrix))


print(determinant(m1))
