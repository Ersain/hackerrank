import numpy
from ZerosAndOnes import zeros_ar, ones_ar


def test_zeros():
    assert (zeros_ar(2, 2, 2) == numpy.array([[[0, 0],
                                               [0, 0]],

                                              [[0, 0],
                                               [0, 0]]])).all()


def test_ones():
    assert (ones_ar(2, 2, 2) == numpy.array([[[1, 1],
                                              [1, 1]],

                                             [[1, 1],
                                              [1, 1]]])).all()


def test_ones_2():
    assert (ones_ar(3, 3, 3) == numpy.array([[[1, 1, 1],
                                              [1, 1, 1],
                                              [1, 1, 1]],

                                             [[1, 1, 1],
                                              [1, 1, 1],
                                              [1, 1, 1]],

                                             [[1, 1, 1],
                                              [1, 1, 1],
                                              [1, 1, 1]]])).all()
