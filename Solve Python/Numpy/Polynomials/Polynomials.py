'''
Problem: Polynomials.
Description: Given coefficients of a polynomial P,
print the value of P at point x.
Points: 20.

'''

import numpy


def p_at_x(p, x):
    return numpy.polyval(p, x)


if __name__ == "__main__":
    p = numpy.array(input().split(), float)
    x = int(input())
    print(p_at_x(p, x))
