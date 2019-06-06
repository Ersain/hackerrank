'''
Problem: Concatenate.
Description: Given a NxM array,
print its transpose and flatten results.
Points: 20.

'''

import numpy

n, m, p = map(int, input().split())
arr1 = numpy.array([input().split() for i in range(n)], int)
arr2 = numpy.array([input().split() for i in range(m)], int)

print(numpy.concatenate((arr1, arr2), axis=0))
