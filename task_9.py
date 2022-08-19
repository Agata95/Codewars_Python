<<<<<<< HEAD
# Valid Parentheses
# Write a function that takes a string of parentheses, and determines if the order of the parentheses is valid.
# The function should return true if the string is valid, and false if it's invalid.
# Examples
# "()"              =>  true
# ")(()))"          =>  false
# "("               =>  false
# "(())((()())())"  =>  true
import re


def valid_parentheses(string):
    tab = []

    for x in string:
        if x in ["(", ")"]:
            tab.append(x)

    total = []
    print(tab)
    if len(tab) == 0:
        return True
    elif len(tab) % 2 == 0:
        for i in range(0, len(tab)):
            if (tab[0] == ')') or (tab[-1] == '('):
                return False
            else:
                if tab[i] == '(':
                    total.append(tab[i])
                else:
                    try:
                        total.remove('(')
                    except:
                        return False
        if len(total) == 0:
            return True
        else:
            return False
    else:
        return False


# print(valid_parentheses(")test)"))
# print(valid_parentheses("  ("))
# print(valid_parentheses(")test"))
# print(valid_parentheses(""))
# print(valid_parentheses("hi())("))
# print(valid_parentheses("hi(hi)()"))
# print(valid_parentheses("())(()"))
print(valid_parentheses("(hdyiwjxvcbp(yt(ivrouxbqmruv)kdfpzcbdwxu"))
=======
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
>>>>>>> b16d7675ac48dd07ed1da093c5ace199d7386a4a
