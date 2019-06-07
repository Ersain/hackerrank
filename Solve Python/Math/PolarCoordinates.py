'''
Problem: Polar Coordinates.
Description: Given a complex number,
convert it into polar.
Points: 10.

'''

from cmath import phase


def count_abs(a, b):
    return abs(complex(a, b))


def count_phase(a, b):
    return phase(complex(a, b))


s = complex(input())
print(abs(s))
print(phase(s))
