import numpy
from FloorCeilAndRint import floor_arr, ceil_arr, rint_arr


def test_floor():
    temp = numpy.array([1.1, 2.2, 3.3, 4.4, 5.5, 6.6, 7.7, 8.8, 9.9])
    assert (floor_arr(temp) == numpy.array(
        [1., 2., 3., 4., 5., 6., 7., 8., 9.])).all()


def test_ceil():
    temp = numpy.array([1.1, 2.2, 3.3, 4.4, 5.5, 6.6, 7.7, 8.8, 9.9])
    assert (ceil_arr(temp) == numpy.array(
        [2.,  3.,  4.,  5.,  6.,  7.,  8.,  9., 10.])).all()


def test_rint():
    temp = numpy.array([1.1, 2.2, 3.3, 4.4, 5.5, 6.6, 7.7, 8.8, 9.9])
    assert (rint_arr(temp) == numpy.array(
        [1.,  2.,  3.,  4.,  6.,  7.,  8.,  9., 10.])).all()
