import numpy
from ArrayMathematics import arr_sum, arr_prod, arr_modulo, arr_exponent, arr_division, arr_difference


def test_sum_diff():
    temp = numpy.array([1, 2, 3, 4])
    assert (arr_sum(temp, temp) == numpy.array([2, 4, 6, 8])).all()
    assert (arr_difference(temp, temp) == numpy.array([0, 0, 0, 0])).all()


def test_div_mod():
    temp = numpy.array([5, 6, 7, 8])
    assert (arr_division(temp, temp) == numpy.array([1, 1, 1, 1])).all()
    assert (arr_modulo(temp, temp) == numpy.array([0, 0, 0, 0])).all()


def test_prod_exp():
    temp = numpy.array([1, 2, 3, 4])
    assert (arr_prod(temp, temp) == numpy.array([1,  4,  9, 16])).all()
    assert (arr_exponent(temp, temp) == numpy.array([1,   4,  27, 256])).all()
