'''
Problem: Dot and Cross.
Description: Given 2 NxM arrays A and B,
print their matrix product.
Points: 20.

'''

import numpy

n = int(input())
arr1 = numpy.array([input().split() for i in range(n)], int)
arr2 = numpy.array([input().split() for i in range(n)], int)

print(numpy.dot(arr1, arr2))
