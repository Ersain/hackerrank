import numpy
from EyeAndIdentity import eye_arr


def test_eye_1():
    assert (eye_arr(3, 3) == numpy.array([[1., 0., 0.],
                                          [0., 1., 0.],
                                          [0., 0., 1.]])).all()


def test_eye_2():
    assert (eye_arr(6, 7) == numpy.array([[1., 0., 0., 0., 0., 0., 0.],
                                          [0., 1., 0., 0., 0., 0., 0.],
                                          [0., 0., 1., 0., 0., 0., 0.],
                                          [0., 0., 0., 1., 0., 0., 0.],
                                          [0., 0., 0., 0., 1., 0., 0.],
                                          [0., 0., 0., 0., 0., 1., 0.]])).all()


def test_eye_3():
    assert (eye_arr(2, 4) == numpy.array([[1., 0., 0., 0.],
                                          [0., 1., 0., 0.]])).all()
