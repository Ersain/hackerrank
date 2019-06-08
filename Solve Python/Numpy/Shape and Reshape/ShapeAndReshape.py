'''
Problem: Shape and Reshape.
Description: Given a list of 9 numbers,
convert this list into 3x3 numpy array and print.
Points: 20.

'''


import numpy


def reshape_ar(ar):
    if len(ar) == 9:
        return numpy.reshape(ar, (3, 3))
    return ar


if __name__ == "__main__":
    arr = numpy.array(input().split(), int)
    print(reshape_ar(arr))
