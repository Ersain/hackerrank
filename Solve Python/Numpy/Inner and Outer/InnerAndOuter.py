'''
Problem: Inner and Outer.
Description: Given 2 arrays,
print their inner and outer product.
Points: 20.

'''

import numpy

arr_a = numpy.array(input().split(), int)
arr_b = numpy.array(input().split(), int)

print(numpy.inner(arr_a, arr_b))
print(numpy.outer(arr_a, arr_b))
