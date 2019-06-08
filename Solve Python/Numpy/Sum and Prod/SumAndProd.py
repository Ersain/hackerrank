'''
Problem: Sum and Prod.
Description: Given a NxM array A,
use sum tool over axis 0 and
find the product of the result.
Points: 20.

'''

import numpy


def prod_of_sum(arr, dir=None):
    return numpy.prod(numpy.sum(arr, axis=dir))


if __name__ == "__main__":
    n, m = map(int, input().split())
    arr = numpy.array([input().split() for i in range(n)], int)
    print(prod_of_sum(arr, 0))
