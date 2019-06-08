import numpy
from Polynomials import p_at_x


def test_polynom_1():
    assert p_at_x([1, -2, 0, 2], 4) == 34


def test_polynom_2():
    assert p_at_x([1, 2, 3], 0) == 3


def test_polynom_3():
    assert p_at_x([1, -2, 0, 2], 1) == 1
