'''
Problem: Transpose and Flatten.
Description: Given a NxM array,
print its transpose and flatten results.

'''

import numpy

n, m = map(int, input().split())
arr = numpy.array([input().split() for i in range(n)], int)

print(numpy.transpose(arr))
print(arr.flatten())
