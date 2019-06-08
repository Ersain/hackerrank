import numpy
from TransposeAndFlatten import transopose_arr, flatten_arr


def test_transpose():
    temp = numpy.reshape([*range(9)], (3, 3))
    assert (transopose_arr(temp) == numpy.array([[0, 3, 6],
                                                 [1, 4, 7],
                                                 [2, 5, 8]])).all()


def test_flatten():
    temp = numpy.reshape([*range(9)], (3, 3))
    assert (flatten_arr(temp) == numpy.array(
        [0, 1, 2, 3, 4, 5, 6, 7, 8])).all()


def test_transpose_flatten():
    temp = numpy.reshape([*range(16)], (4, 4))
    assert (transopose_arr(temp) == numpy.array([[0,  4,  8, 12],
                                                 [1,  5,  9, 13],
                                                 [2,  6, 10, 14],
                                                 [3,  7, 11, 15]])).all()
