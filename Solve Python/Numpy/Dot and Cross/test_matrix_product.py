import numpy
from DotAndCross import matrix_product


def test_matrix_prod_1():
    temp = numpy.reshape([*range(1, 5)], (2, 2))
    temp2 = numpy.reshape([*range(1, 5)], (2, 2))

    assert (matrix_product(temp, temp2) == numpy.array([[7, 10],
                                                        [15, 22]])).all()


def test_matrix_prod_2():
    temp = numpy.reshape([*range(1, 10)], (3, 3))

    assert (matrix_product(temp, temp) == numpy.array([[30,  36,  42],
                                                       [66,  81,  96],
                                                       [102, 126, 150]])).all()


def test_matrix_prod_3():
    temp = numpy.reshape([*range(1, 17)], (4, 4))

    assert (matrix_product(temp, temp) == numpy.array([[90, 100, 110, 120],
                                                       [202, 228, 254, 280],
                                                       [314, 356, 398, 440],
                                                       [426, 484, 542, 600]])).all()
