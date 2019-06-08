'''
Problem: Array Mathematics.
Description: Given 2 NxM arrays A and B,
print the following:
A+B, A-B,
A*B, A/B,
A % B, A**B.

Points: 20.

'''

import numpy


def arr_sum(arr1, arr2):
    return (arr1 + arr2)


def arr_difference(arr1, arr2):
    return (arr1 - arr2)


def arr_prod(arr1, arr2):
    return (arr1 * arr2)


def arr_division(arr1, arr2):
    return (arr1 // arr2)


def arr_modulo(arr1, arr2):
    return (arr1 % arr2)


def arr_exponent(arr1, arr2):
    return (arr1 ** arr2)


if __name__ == "__main__":
    n, m = map(int, input().split())
    arr1 = numpy.array([input().split() for i in range(n)], int)
    arr2 = numpy.array([input().split() for i in range(n)], int)

    print(arr_sum(arr1, arr2))
    print(arr_difference(arr1, arr2))
    print(arr_prod(arr1, arr2))
    print(arr_division(arr1, arr2))
    print(arr_modulo(arr1, arr2))
    print(arr_exponent(arr1, arr2))
