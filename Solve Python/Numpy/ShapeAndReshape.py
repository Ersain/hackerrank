'''
Problem: Shape and Reshape.
Description: Given a list of 9 numbers,
convert this list into 3x3 numpy array and print.
Points: 20.

'''


import numpy

arr = numpy.array(input().split(), int)
print(numpy.reshape(arr, (3, 3)))
