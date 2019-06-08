'''
Problem: Zeros and Ones.
Description: Given the 3D shape of an array,
print it using numpy.zeros and numpy.ones.
Points: 20.

'''

import numpy


def zeros_ar(x, y, z):
    return numpy.zeros((x, y, z), dtype=numpy.int)


def ones_ar(x, y, z):
    return numpy.ones((x, y, z), dtype=numpy.int)


if __name__ == "__main__":
    x, y, z = map(int, input().split())
    print(zeros_ar(x, y, z))
    print(ones_ar(x, y, z))
