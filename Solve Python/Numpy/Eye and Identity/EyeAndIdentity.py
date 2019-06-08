'''
Problem: Eye and Identity.
Description: Given 2 integers n and m,
print NxM matrix with its main diagonal elements
as 1s and 0s elsewhere.
Points: 20.

'''

import numpy


def eye_arr(n, m):
    return numpy.eye(n, m)


if __name__ == "__main__":
    numpy.set_printoptions(sign=' ')

    n, m = map(int, input().split())
    print(eye_arr(n, m))
