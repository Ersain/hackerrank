'''
Problem: Polynomials.
Description: Given coefficients of a polynomial P,
print the value of P at point x.
Points: 20.

'''

import numpy

p = numpy.array(input().split(), float)
x = int(input())
print(numpy.polyval(p, x))
