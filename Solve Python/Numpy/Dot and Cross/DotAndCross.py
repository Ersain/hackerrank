'''
Problem: Dot and Cross.
Description: Given 2 NxM arrays A and B,
print their matrix product.
Points: 20.

'''

import numpy


def matrix_product(arr_1, arr_2):
    return numpy.dot(arr_1, arr_2)


if __name__ == "__main__":
    n = int(input())
    arr1 = numpy.array([input().split() for i in range(n)], int)
    arr2 = numpy.array([input().split() for i in range(n)], int)

    print(matrix_product(arr1, arr2))
