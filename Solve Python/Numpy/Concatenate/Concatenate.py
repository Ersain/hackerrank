'''
Problem: Concatenate.
Description: Given a NxM array,
print its transpose and flatten results.
Points: 20.

'''

import numpy


def concat_arrs(arr_1, arr_2, axis=None):
    return numpy.concatenate((arr_1, arr_2), axis)


if __name__ == "__main__":
    n, m, p = map(int, input().split())
    arr1 = numpy.array([input().split() for i in range(n)], int)
    arr2 = numpy.array([input().split() for i in range(m)], int)

    print(concat_arrs(arr1, arr2, axis=0))
