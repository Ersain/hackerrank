'''
Problem: Min and Max.
Description: Given a NxM array A,
use the min function over axis 1 and
find the max of that.

'''

import numpy

n, m = map(int, input().split())
arr = numpy.array([input().split() for i in range(n)], int)

print(numpy.max(numpy.min(arr, axis=1)))
