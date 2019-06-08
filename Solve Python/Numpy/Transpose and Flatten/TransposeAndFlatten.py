'''
Problem: Transpose and Flatten.
Description: Given a NxM array,
print its transpose and flatten results.
Points: 20.

'''

import numpy


def transopose_arr(ar):
    return numpy.transpose(ar)


def flatten_arr(ar):
    return ar.flatten()


if __name__ == "__main__":
    n, m = map(int, input().split())
    arr = numpy.array([input().split() for i in range(n)], int)

    print(transopose_arr(arr))
    print(flatten_arr(arr))
