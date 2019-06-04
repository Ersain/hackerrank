'''
Problem: Polar Coordinates.
Description: Given a complex number,
convert it into polar.

'''

from cmath import phase

s = complex(input())
print(abs(s))
print(phase(s))
