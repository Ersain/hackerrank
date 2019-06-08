import numpy
from InnerAndOuter import inner_prod, outer_prod


def test_inner():
    temp = numpy.array([0, 1])
    temp2 = numpy.array([3, 4])
    assert inner_prod(temp, temp2) == 4


def test_outer():
    temp = numpy.array([0, 1])
    temp2 = numpy.array([3, 4])
    assert (outer_prod(temp, temp2) == numpy.array([[0, 0],
                                                    [3, 4]])).all()


def test_outer_2():
    temp = numpy.array([[1, 2, 3], [4, 5, 6]])
    temp2 = numpy.array([[7, 8, 9], [5, 7, 2]])
    assert (outer_prod(temp, temp2) == numpy.array([[7,  8,  9,  5,  7,  2],
                                                    [14, 16, 18, 10, 14,  4],
                                                    [21, 24, 27, 15, 21,  6],
                                                    [28, 32, 36, 20, 28,  8],
                                                    [35, 40, 45, 25, 35, 10],
                                                    [42, 48, 54, 30, 42, 12]])).all()
