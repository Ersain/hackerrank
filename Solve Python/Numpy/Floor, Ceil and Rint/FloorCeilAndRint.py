'''
Problem: Floor, Ceil and Rint.
Description: Given 1D array A,
print the floor, ceil, rint
of all the elements of A.
Points: 20.

'''

import numpy
numpy.set_printoptions(sign=' ')


def floor_arr(arr):
    return numpy.floor(arr)


def ceil_arr(arr):
    return numpy.ceil(arr)


def rint_arr(arr):
    return numpy.rint(arr)


if __name__ == "__main__":
    arr = numpy.array(input().split(), float)
    print(floor_arr(arr))
    print(ceil_arr(arr))
    print(rint_arr(arr))
