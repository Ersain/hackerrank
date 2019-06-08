import numpy
from MinAndMax import max_of_min


def test_maxmin_1():
    temp = numpy.reshape([2, 5, 3, 7, 1, 3, 4, 0], (4, 2))
    assert max_of_min(temp, 1) == 3


def test_maxmin_2():
    temp = numpy.reshape([*range(1, 10)], (3, 3))
    assert max_of_min(temp, 1) == 7


def test_maxmin_3():
    temp = numpy.reshape([*range(10, 19)], (3, 3))
    assert max_of_min(temp, 1) == 16
