'''
Problem: Floor, Ceil and Rint.
Description: Given 1D array A,
print the floor, ceil, rint
of all the elements of A.
Points: 20.

'''

import numpy

numpy.set_printoptions(sign=' ')

arr = numpy.array(input().split(), float)
print(numpy.floor(arr))
print(numpy.ceil(arr))
print(numpy.rint(arr))
