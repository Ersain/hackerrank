'''
Problem: Arrays.
Description: Given a list of numbers,
print a reversed numpy array.
Points: 20.

'''

import numpy


def arrays(arr):
    return numpy.array(arr[::-1], float)
