import numpy
from ShapeAndReshape import reshape_ar


def test_shape_reshape_1():
    temp = numpy.array([*range(9)])
    print(temp)
    assert (reshape_ar(temp) == numpy.array([[0, 1, 2],
                                             [3, 4, 5],
                                             [6, 7, 8]])).all()


def test_shape_reshape_2():
    temp = numpy.array([*range(8)])
    print(temp)
    assert (reshape_ar(temp) == temp).all()


def test_shape_reshape_3():
    temp = numpy.array([7, 0, 10, 4, 66, 8, 9, 1, 123])
    print(temp)
    assert (reshape_ar(temp) == numpy.array([[7,   0,  10],
                                             [4,  66,   8],
                                             [9,   1, 123]])).all()
