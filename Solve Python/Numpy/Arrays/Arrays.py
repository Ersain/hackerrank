'''
Problem: Arrays.
Description: Given a list of numbers,
print a reversed numpy array.
Points: 20.

'''

import numpy


def reverse_array(arr):
    return numpy.array(arr[::-1], float)


if __name__ == "__main__":
    arr = input().strip().split(' ')
    result = reverse_array(arr)
    print(result)
