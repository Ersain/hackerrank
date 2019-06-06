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


# s = complex(input())
# print(abs(s))
# print(phase(s))


def test_abs():
    assert count_abs(3, 4) == 5
    assert count_abs(6, 8) == 10


def test_phase_1():
    assert count_phase(3, 4) > 0
    assert count_phase(6, 8) > 0


def test_phase_2():
    assert count_phase(6, 0) == 0
    assert count_phase(0, 8) > 1
