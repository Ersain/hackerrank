'''
Problem: Eye and Identity.
Description: Given 2 integers n and m,
print NxM matrix with its main diagonal elements
as 1s and 0s elsewhere.

'''

import numpy

numpy.set_printoptions(sign=' ')

n, m = map(int, input().split())
print(numpy.eye(n, m))
