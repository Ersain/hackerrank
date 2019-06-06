'''
Problem: Sum and Prod.
Description: Given a NxM array A,
use sum tool over axis 0 and
find the product of the result.
Points: 20.

'''

import numpy

n, m = map(int, input().split())
arr = numpy.array([input().split() for i in range(n)], int)
print(numpy.prod(numpy.sum(arr, axis=0)))
