'''
Problem: Inner and Outer.
Description: Given 2 arrays,
print their inner and outer product.
Points: 20.

'''

import numpy


def inner_prod(arr1, arr2):
    return numpy.inner(arr1, arr2)


def outer_prod(arr1, arr2):
    return numpy.outer(arr1, arr2)


if __name__ == "__main__":
    arr_a = numpy.array(input().split(), int)
    arr_b = numpy.array(input().split(), int)

    print(inner_prod(arr_a, arr_b))
    print(outer_prod(arr_a, arr_b))
