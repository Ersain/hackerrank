import numpy
from SumAndProd import prod_of_sum


def test_sumprod_1():
    temp = numpy.array([[1, 2], [3, 4]])
    assert prod_of_sum(temp, 0) == 24


def test_sumprod_2():
    temp = numpy.array([[1, 2, 3], [4, 5, 6]])
    assert prod_of_sum(temp, 0) == 315


def test_sumprod_3():
    temp = numpy.array([[1, 2, 3, 4], [5, 6, 7, 8]])
    assert prod_of_sum(temp, 0) == 5760
