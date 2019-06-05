'''
Problem: Zeros and Ones.
Description: Given the 3D shape of an array,
print it using numpy.zeros and numpy.ones.

'''

import numpy

coords = tuple(map(int, input().split()))
print(numpy.zeros(coords, dtype=numpy.int))
print(numpy.ones(coords, dtype=numpy.int))
