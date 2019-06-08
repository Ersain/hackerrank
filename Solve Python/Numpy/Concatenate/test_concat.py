import numpy
from Concatenate import concat_arrs


def test_concat_1():
    temp = numpy.reshape([*range(8)], (2, 4))
    temp2 = numpy.reshape([*range(8, 16)], (2, 4))
    assert (concat_arrs(temp, temp2, 1) == numpy.array([[0,  1,  2,  3,  8,  9, 10, 11],
                                                        [4,  5,  6,  7, 12, 13, 14, 15]])).all()


def test_concat_2():
    temp = numpy.reshape([*range(8)], (4, 2))
    temp2 = numpy.reshape([*range(8, 16)], (4, 2))
    assert (concat_arrs(temp, temp2, 1) == numpy.array([[0,  1,  8,  9],
                                                        [2,  3, 10, 11],
                                                        [4,  5, 12, 13],
                                                        [6,  7, 14, 15]])).all()


def test_concat_3():
    temp = numpy.array([*range(9)])
    temp2 = numpy.array([*range(9, 15)])
    assert (concat_arrs(temp, temp2) == numpy.array(
        [0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12, 13, 14])).all()
