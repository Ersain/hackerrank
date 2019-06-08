'''
Problem: Min and Max.
Description: Given a NxM array A,
use the min function over axis 1 and
find the max of that.
Points: 20.

'''

import numpy


def max_of_min(arr, dir=None):
    return numpy.max(numpy.min(arr, axis=dir))


if __name__ == "__main__":
    n, m = map(int, input().split())
    arr = numpy.array([input().split() for i in range(n)], int)

    print(max_of_min(arr, 1))
